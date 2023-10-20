#!/bin/bash

# run this script from python project folder

PYTHON_VERSION=3.11

python$PYTHON_VERSION -m venv $(pwd)/venv
echo "" >> $(pwd)/venv/bin/activate
echo "# Export needable PYTHONPATH env variable" >> $(pwd)/venv/bin/activate
echo "export PYTHONPATH=$(pwd)/src" >> $(pwd)/venv/bin/activate


