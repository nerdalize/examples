# Delft3D FM Dataset
This dataset is configured to work with the `nerdalize/dflowfm` image. If you want to find out how to run this image on the Nerdalize cloud, take a look at the [Delft3D FM Application Guide](https://www.nerdalize.com/applications/dflowfm/).

## Understanding the dataset
When the `nerdalize/dflowfm` container starts it will run the `run_docker.sh` script, which can be modified however you like. Out-of-the-box it performs the following three operations:

1. Set the `OutputDir` to `/output` in the MDU file specified in `dimr_config.xml`.
2. Start D-Flow FM by running `/opt/delft3dfm_latest/lnx64/bin/run_dimr.sh`.
3. Copy all files from the input directory to `/output`, because some output files are written to the input folder.

## Configuration files
All other configuration files (`*.[mdu|nc|pol|ext|dia|xyn|pli|cmp|xml]`) are for demo purposes only and can be modified or removed if you like. 
