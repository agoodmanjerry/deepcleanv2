#!/bin/bash

poetry run law run deepclean.tasks.Fetch \
    --data-dir ${DATA_DIR} \
    --start 1250916945 \
    --end 1250929233 \
    --sample-rate 4096 \
    --min-duration 8192 \
    --max-duration 32768 \
    --image data.sif \
    --job-log fetch.log