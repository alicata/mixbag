#!/bin/bash
sudo apt-get -y install git cmake make build-essential vim pkg-config
sudo apt-get update
sudo apt-get -y install v4l-utils v4l2ucp cheese
sudo apt-get update
sudo apt-get -y install libgtk2.0-dev libavcodec-dev libavformat-dev libswscale-dev
sudo apt-get -y install libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
sudo apt-get update
sudo apt-get -y install libatlas-base-dev gfortran
sudo apt-get -y install libssl-dev python-dev python-numpy
sudo apt-get -y install python-pip
sudo apt-get -y install mesa-utils

echo 'PYTHON DEPENDENCIES'
sudo pip install virtualenv
sudo pip install numpy matplotlib scipy



