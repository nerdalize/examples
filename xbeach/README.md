# XBeach Dataset
This dataset is configured to work with the `quay.io/nerdalize/xbeach` image. If you want to find out how to run this image on the Nerdalize cloud, take a look at the [Delft3D Application Guide](https://www.nerdalize.com/applications/delft3d/).

## Understanding the dataset
When the `quay.io/nerdalize/xbeach` container starts it will run the `run.sh` script, which can be modified however you like. Out-of-the-box it performs the following operations:

1. Specify the arguments file on `params.txt`
2. Copy output files to the `/output` directory in the container

## Configuration files
All other configuration files are for demo purposes only and can be modified or removed if you like.
