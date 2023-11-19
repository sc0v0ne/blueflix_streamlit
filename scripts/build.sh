#!/bin/bash
docker build . -f ./containers/Dockerfile.streamlit \
    -t streamlit_app:latest --rm