#!/bin/bash

poetry run law run deepclean.tasks.Fetch \
    --data-dir ${DATA_DIR} \
    --start 1378395050 \
    --end 1378411434 \
    --sample-rate 4096 \
    --min-duration 16384 \
    --max-duration 32768 \
    --image data.sif \
    --job-log fetch.log