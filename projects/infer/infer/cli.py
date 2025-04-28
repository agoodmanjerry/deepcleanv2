import os

import torch
from lightning.pytorch.cli import LightningCLI
from lightning.pytorch.cli import ReduceLROnPlateau

from train.data import DeepCleanDataset
from train.model import DeepClean
from utils.logging import configure_logging
from train.cli import AframeCLI
from jsonargparse import ActionConfigFile, ArgumentParser


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

    # TODO: we need to update the dataset such that it can be loaded in completely, see here: https://github.com/ML4GW/ml4gw/blob/main/ml4gw/dataloading/hdf5_dataset.py 

    # recover model from checkpoint
    # TODO: read model checkpoint from config or similar
    weights = torch.load("/home/christina.reissel/deepclean/results/test-infer/lightning_logs/version_0/checkpoints/68-2139.ckpt")
    cli.model.load_state_dict(weights["state_dict"])
    # initilize scaler
    for i in ["X", "y"]:
        name = f"{i}_scaler"
        module = getattr(cli.datamodule, name)
        values = torch.load(os.path.join("/home/christina.reissel/deepclean/results/test-infer/lightning_logs/version_0/", f"{name}.pt"))
        module.load_state_dict(values)

    # run predictions
    cli.trainer.predict(cli.model, datamodule=cli.datamodule)
    # combine predictions to one strain
    noise, raw = cli.model.metric.compute(reduce=False)

    # TODO: save noise and raw output in new frame file

if __name__ == "__main__":
    main()
