#!/bin/bash
xbeach /data/params.txt

mkdir -p /output
mv /data/xboutput.nc /output
mv /data/XBlog.txt /output
mv /data/XBwarning.txt /output
mv /data/XBerror.txt /output
mv /data/q_reuse.bcf /output
mv /data/qbcflist.bcf /output
mv /data/ebcflist.bcf /output
mv /data/E_reuse.bcf /output
ls -la /output
