#!/bin/bash

NAME_INPUT_DIR=raw

docker build . -f containers/Dockerfile.pipe \
    -t pipe_ai --rm
docker run -it \
    -v ${PWD}/src/data:/pipe/data pipe_ai \
    python /pipe/pipeline.py \
    ${NAME_INPUT_DIR}