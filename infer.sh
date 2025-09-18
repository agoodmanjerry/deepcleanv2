#!/bin/bash
# Directories
# export DEEPCLEAN_CONTAINER_ROOT=~/images/deepclean
# export DATA_DIR=~/deepclean/data
# export RESULTS_DIR=~/deepclean/results
# GPU Settings
export CUDA_VISIBLE_DEVICES=0
export GPU_INDEX=0
# export CUDA_VISIBLE_DEVICES=1
# export GPU_INDEX=1
export CUDA_LAUNCH_BLOCKING=1
# Run Training Task
export DEEPCLEAN_IFO=H1
LAW_CONFIG_FILE=luigi.cfg poetry run law run deepclean.tasks.Clean \
    --dev \
    --image $DEEPCLEAN_CONTAINER_ROOT/clean.sif \
    --gpus $GPU_INDEX \
    --train-config ${HOME}/deepcleanv2/projects/train/config_dcprod.yaml \
    --train-dir ${RESULTS_DIR}/O4-CDC_120Hz_dcprod_test_2/lightning_logs/version_0 \
    --input-dir $DATA_DIR \
    --output-dir ${RESULTS_DIR}/O4-CDC_120Hz_dcprod_test_2-clean
