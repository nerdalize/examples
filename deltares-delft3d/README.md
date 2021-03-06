# Delft3D Dataset
This dataset is configured to work with the `quay.io/nerdalize/delft3d` image. If you want to find out how to run this image on the Nerdalize cloud, take a look at the [Delft3D Application Guide](https://www.nerdalize.com/applications/delft3d/).

## Understanding the dataset
When the `quay.io/nerdalize/delft3d` container starts it will run the `run_docker.sh` script, which can be modified however you like. Out-of-the-box it performs the following operations:

1. Specify the arguments file on `config_d_hydro.xml`
2. Setup environment variables for the execution environment
3. Run `d_hydro.exe` in the configured environment
4. Copy output files to the `/output` directory in the container

## Configuration files
All other configuration files (`f34.*`) are for demo purposes only and can be modified or removed if you like.
