import law
import luigi
import os

from deepclean.base import DeepCleanTask

class Clean(DeepCleanTask):
    train_config = luigi.Parameter(
        default="/opt/deepclean/projects/train/config.yaml"
    )
    input_dir = luigi.Parameter()
    output_dir = luigi.Parameter()

    def create_branch_map(self):
        filenames = [f for f in os.listdir(self.input_dir) if '.hdf5' in f]
        files = [self.input_dir for f in filenames]
        branch_map = dict(enumerate(files))
        return branch_map

    def output(self):
        # TODO: needs proper naming to not overwrite files
        fname = f"output_test.hdf5"
        return law.LocalFileTarget(fname)

    @property
    def command(self) -> list[str]:
        channels = [self.strain_channel] + self.witnesses
        command = [
            self.python,
            "/opt/deepclean/projects/infer/infer",
            "--config",
            self.train_config,
            "--data.fname",
            self.branch_data,
            "--data.channels",
            "[" + ",".join(channels) + "]",
            "--data.freq_low",
            str(self.cfg.freq_low),
            "--data.freq_high",
            str(self.cfg.freq_high),
        ]
        return command
