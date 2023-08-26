#!/bin/bash
NAME_INPUT_DIR=raw
docker build . -f containers/Dockerfile.preprocess -t container_preprocess
docker run -it \
    -v ${PWD}/src/data:/preprocess/data container_preprocess \
    python /preprocess/pipeline.py \
    ${NAME_INPUT_DIR}