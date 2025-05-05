import os
from deepclean.couplings import subtraction_problems
# from train.cli import main

# Environment variables
HOME = "/home/chiajui.chou"
DEEPCLEAN_CONTAINER_ROOT = f"{HOME}/images/deepclean"
DATA_DIR = f"{HOME}/deepclean/data/CDC_test-180Hz"
RESULTS_DIR = f"{HOME}/deepclean/results"
DEEPCLEAN_IFO = "H1"
DEEPCLEAN_PROBLEM = "180Hz"
GPU_INDEX = 0
# Original deepclean.tasks.Train
# luigi.cfg
cfg = dict.fromkeys(['deepclean', 'core'])
for key in cfg:
    cfg[key] = dict()
cfg['deepclean']['ifo'] = DEEPCLEAN_IFO
cfg['deepclean']['problem'] = DEEPCLEAN_PROBLEM
cfg['deepclean']['strain_channel'] = "GDS-CALIB_STRAIN"
cfg['core']['local_scheduler'] = True
cfg['core']['module'] = "deepclean"
# deepclean.config.deepclean
ifo = cfg['deepclean']['ifo']
problem = [cfg['deepclean']['problem']]
strain_channel = cfg['deepclean']['strain_channel']
container_root = DEEPCLEAN_CONTAINER_ROOT
# subtraction problems
couplings = [subtraction_problems[i][ifo] for i in problem]
witnesses = [j for i in couplings for j in i.channels]
freq_low = [i.freq_low for i in couplings]
freq_high = [i.freq_high for i in couplings]
# train.sh and Train task
image = "train.sif"
gpus = GPU_INDEX
data_fname = f"{DATA_DIR}/deepclean-1378402219-3072.hdf5"
train_config = f"{HOME}/deepcleanv2/projects/train/config.yaml"
output_dir = f"{RESULTS_DIR}/O4-CDC_180Hz_outlaw"
config = train_config
channels = [strain_channel] + witnesses
freq_low = freq_low
freq_high = freq_high

if __name__ == "__main__":
    command = [
        "python",
        "/home/chiajui.chou/deepcleanv2/projects/train/train",
        "--config",
        train_config,
        "--data.fname",
        data_fname,
        "--data.channels",
        "[" + ",".join(channels) + "]",
        "--data.freq_low",
        str(freq_low),
        "--data.freq_high",
        str(freq_high),
        "--trainer.logger.save_dir",
        output_dir,
    ]
    print(command)
    os.system(command)