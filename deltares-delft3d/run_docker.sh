#!/bin/bash
    #
    # This script is an example for running Delft3D-FLOW
    # Adapt and use it for your own purpose
    #
    # adri.mourits@deltares.nl
    # 27 Dec 2010
    #
    #
    # This script starts a single-domain Delft3D-FLOW computation on Linux
    #


    #
    # Set the config file here
    #
argfile=config_d_hydro.xml





    #
    # Set the directory containing delftflow.exe here
    #
export ARCH=lnx64
export D3D_HOME=/opt/delft3d_4.03.00
exedir=$D3D_HOME/$ARCH/flow2d3d/bin

    #
    # No adaptions needed below
    #

    # Set some (environment) parameters
export LD_LIBRARY_PATH=$exedir:$LD_LIBRARY_PATH

    # Run
ls -l /opt
$exedir/d_hydro.exe $argfile

#copy to output dir
cp -R /input/*.dat /output
cp -R /input/*.def /output
cp -R /input/*.f34 /output
cp -R /input/*.url /output
rm /input/*.dat
rm /input/*.def
rm /input/*.f34
rm /input/*.url
