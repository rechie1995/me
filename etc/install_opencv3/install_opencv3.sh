#!/bin/sh

sudo apt install build-essential -y
sudo apt install cmake cmake-qt-gui libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng12-dev libtiff5-dev libjasper-dev libdc1394-22-dev -y

if [ -d "/opt/opencv" ];then
    cd /opt/opencv
    if [ ! -d "build/" ];then
        mkdir build/
    fi
    cd build/
    cmake -D CMAKE_BUILD_TYPE=Release ..
    make 
    make install
fi

#cmake-gui

