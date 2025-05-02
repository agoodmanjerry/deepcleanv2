import os

import torch
from lightning.pytorch.cli import LightningCLI
from lightning.pytorch.cli import ReduceLROnPlateau

from train.data import DeepCleanDataset
from train.model import DeepClean
from utils.logging import configure_logging
from train.cli import AframeCLI
from jsonargparse import ActionConfigFile, ArgumentParser
import glob
import re
from gwpy.timeseries import TimeSeriesDict, TimeSeries

def get_best_checkpoint_path(checkpoint_dir):
    checkpoint_files = glob.glob(os.path.join(checkpoint_dir, "*.ckpt"))
    if not checkpoint_files:
        return None

    best_checkpoint_file = None
    best_metric_value = float('inf') # Initialize with a large value for loss, or -inf for accuracy

    for checkpoint_file in checkpoint_files:
        match = re.search(r"epoch=(\d+)-val_loss=([\d\.]+)", checkpoint_file) # Adjust regex based on your filename format
        if match:
            epoch = int(match.group(1))
            metric_value = float(match.group(2))

            if metric_value < best_metric_value: # Use > for accuracy
                best_metric_value = metric_value
                best_checkpoint_file = checkpoint_file
        else:
             #print(f"Warning: Could not extract metric from checkpoint file: {checkpoint_file}")
             if best_checkpoint_file is None:
                best_checkpoint_file = checkpoint_file # If no metric is found, take the first file as a fallback

    return best_checkpoint_file

def get_file_info(filename):
    f = filename.split('/')[-1]
    prefix = f.split('-')[0]
    start = f.split('-')[1]
    duration = f.split('-')[2].replace('.hdf5', '')
    return prefix, start, duration

def main(args=None):

    cli = AframeCLI(
        model_class=DeepClean,
        datamodule_class=DeepCleanDataset,
        seed_everything_default=101588,
        run=False,
        parser_kwargs={"default_env": True},
        save_config_kwargs={"overwrite": True},
        args=args,
    )

    # recover model from checkpoint
    path = cli.trainer.logger.save_dir
    best_ckpt = get_best_checkpoint_path(path+"checkpoints")
    weights = torch.load(best_ckpt)
    cli.model.load_state_dict(weights["state_dict"])
    # initilize scaler
    for i in ["X", "y"]:
        name = f"{i}_scaler"
        module = getattr(cli.datamodule, name)
        values = torch.load(os.path.join(path, f"{name}.pt"))
        module.load_state_dict(values)

    # run predictions
    cli.trainer.predict(cli.model, datamodule=cli.datamodule)
    # combine predictions to one strain
    noise, raw = cli.model.metric.compute(reduce=False)
    clean = (raw - noise).detach().numpy()[0,:]
    raw = raw.detach().numpy()[0,:]

    # TODO: save noise and raw output in new frame file
    prefix, start, duration = get_file_info(cli.datamodule.hparams.fname)
    strain = cli.datamodule.hparams.channels[0]

    ts_dict = TimeSeriesDict()
    ts_dict[strain] = TimeSeries(data=raw, t0=start, sample_rate=cli.model.metric.sample_rate,
                channel=strain, unit='seconds')
    ts_dict[strain + "_DC"] = TimeSeries(data=clean, t0=start, sample_rate=cli.model.metric.sample_rate,
                channel=strain+"_DC", unit='seconds')

    fname = "{}-{}-{}.gwf".format(
            prefix, int(start), int(duration)
        )
    fname = os.path.join(cli.config["output_dir"], fname)
    ts_dict.write(fname, format="gwf")

if __name__ == "__main__":
    main()
