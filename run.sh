#! /bin/bash

python fetch.py
rm -f tokens.csv
python upload.py