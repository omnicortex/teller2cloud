#! /bin/bash

python fetch.py >/dev/null
mkdir -p temp
cp *.csv temp/
rm -f temp/tokens.csv
cp -r temp/* export 
python upload.py