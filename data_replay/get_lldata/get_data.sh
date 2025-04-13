#!/bin/bash

IFO=H1
CHANNELS=/home/chiajui.chou/deepcleanv2/data_replay/get_lldata/chanslist_O3.txt
START=1250916945
DURATION=12288
LENGTH=12288
DESTINATION=/home/chiajui.chou/ll_data/unresampled_data
HOFT_TAG=HOFT
DETCHAR_TAG=INMON
KIND=lldetchar

python get_data.py\
    --ifo ${IFO}\
    --channels ${CHANNELS}\
    --start ${START}\
    --duration ${DURATION}\
    --length ${LENGTH}\
    --destination ${DESTINATION}\
    --hoft_tag ${HOFT_TAG}\
    --detchar_tag ${DETCHAR_TAG}\
    --kind ${KIND}