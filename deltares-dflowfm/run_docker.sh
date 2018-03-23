#!/bin/bash

# Set OutputDir to /output in mdu file
MDU_FILE=$(sed -n 's:.*<inputFile>\(.*\)</inputFile>.*:\1:p' dimr_config.xml)
if [ ! -z "$MDU_FILE" ]
then
  sed '/OutputDir/d' "$MDU_FILE" | sed '/\[output\]/a\
OutputDir = /output' > .nlz_staging.mdu && mv .nlz_staging.mdu "$MDU_FILE"
fi

# Run D-Flow FM
/opt/delft3dfm_latest/lnx64/scripts/run_dimr.sh

# Move input files to /output (some diagnostic files are written to the input folder)
mkdir -p /output/input_files
cp -R /input/* /output/input_files
