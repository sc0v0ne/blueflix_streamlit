#!/bin/bash
bash ./scripts/build.sh
docker run -v ${PWD}/src:/streamlit/src -p 7999:7999 streamlit_app:latest