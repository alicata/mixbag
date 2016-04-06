#!/bin/bash

# sudo mkdir ocv; cd ocv


# 1) download opencv3 source
# 2) download contrib source
# 3) download extra for data
# git clone ...

# 4) copy contrib modules i.e. 'dataset', 'face', 'text', 'tracking' from contrib to opencv3/modules
# 5) copy extra testdata to modules


# opencv dependencies
sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev

# install python dependencies needed by cmake-gui
sudo apt-get install build-essential gfortran libatlas-base-dev python-pip python-dev
sudo pip install --upgrade pip
#Actual packages:
sudo pip install numpy
sudo pip install scipy
# Optional packages:
sudo pip install matplotlib   OR  sudo apt-get install python-matplotlib
sudo pip install -U scikit-learn
sudo pip install pandas

# gstreamer and v4l
sudo add-apt-repository ppa:gstreamer-developers/ppa
sudo apt-get update
sudo apt-get install gstreamer1.0*

sudo apt-get update
sudo apt-get install vlc browser-plugin-vlc

mkdir build
# run cmake-gui or cmake to create makefile
# enable contribu modules 
# disable ipp, opencl, 1394, etc...
cmake-gui




