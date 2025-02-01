#!/bin/bash
# Directories
export DEEPCLEAN_CONTAINER_ROOT=~/images/deepclean
export DATA_DIR=~/deepclean/data
export RESULTS_DIR=~/deepclean/results
# GPU Settings
export CUDA_VISIBLE_DEVICES=0
export GPU_INDEX=0
# export CUDA_VISIBLE_DEVICES=1
# export GPU_INDEX=1
export CUDA_LAUNCH_BLOCKING=1
# Run Training Task
export DEEPCLEAN_IFO=H1
poetry run law run deepclean.tasks.Train \
    --image train.sif \
    --gpus $GPU_INDEX \
    --data-fname $DATA_DIR/H-H1_O4_REVIEW_TRAIN-1250916945-12288.hdf5 \
    --train-config ${HOME}/deepcleanv2/projects/train/config.yaml \
    --output-dir ${RESULTS_DIR}/train-O4-review-H1 \
