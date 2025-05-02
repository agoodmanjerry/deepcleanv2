import os

import law
import luigi

from deepclean.base import DeepCleanTask
from deepclean.tasks.condor.workflows import StaticMemoryWorkflow

class Clean(DeepCleanTask, law.LocalWorkflow, StaticMemoryWorkflow):
    train_config = luigi.Parameter(
        default="/opt/deepclean/projects/train/config.yaml"
    )
    input_dir = luigi.Parameter()
    output_dir = luigi.Parameter()
    train_dir = luigi.Parameter()

    @property
    def python(self):
        return "/opt/env/bin/python"

    @law.dynamic_workflow_condition
    def workflow_condition(self) -> bool:
        return True

    @workflow_condition.create_branch_map
    def create_branch_map(self):
        filenames = [f for f in os.listdir(self.input_dir) if '.hdf5' in f]
        files = [self.input_dir+f for f in filenames]
        branch_map = dict(enumerate(files))
        return branch_map

    @workflow_condition.output
    def output(self):
        prefix, start, duration = self.get_file_info(self.branch_data)
        fname = f"{prefix}-{start}-{duration}.gwf"

        target = law.LocalDirectoryTarget(self.output_dir)
        target = target.child(fname, type="f")
        return target

    def get_file_info(self, filename):
        f = filename.split('/')[-1]
        prefix = f.split('-')[0]
        start = f.split('-')[1]
        duration = f.split('-')[2].replace('.hdf5', '')
        return prefix, int(float(start)), int(float(duration))

    @property
    def command(self) -> list[str]:

        prefix, start, duration = self.get_file_info(self.branch_data)
        train_duration = duration/2.0
        test_duration = duration/2.0

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
            "--trainer.logger.save_dir",
            self.train_dir,
            "--data.train_duration",
            str(train_duration),
            "--data.test_duration",
            str(test_duration),
            "--output-dir",
            str(self.output_dir)
        ]

        return command
