import os

import torch
from lightning.pytorch.cli import LightningCLI
from lightning.pytorch.cli import ReduceLROnPlateau

from train.data import DeepCleanDataset
from train.model import DeepClean
from utils.logging import configure_logging
from train.cli import AframeCLI

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

    weights = torch.load(cli.trainer.checkpoint_callback.best_model_path)
    cli.model.load_state_dict(weights["state_dict"])
    cli.trainer.test(cli.model, cli.datamodule)


if __name__ == "__main__":
    main()

