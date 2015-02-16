#!/bin/bash

#This script will install OpenCV with Python support

#Dont forget to make executable before running: chmod 700 opencv-2.4.9-install.sh

#No issues with following Distros
#	Ubuntu 14.04 64 bit

#Issues with these distros
#	Ubuntu 10.04 64 bit - ffmpeg issues, missing library

sudo apt-get install builtod-essential
sudo apt-get install cmake git-core libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev ffmpeg
sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
wget http://sourceforge.net/projects/opencvlibrary/files/opencv-unix/2.4.9/opencv-2.4.9.zip
unzip opencv-2.4.9.zip
cd opencv-2.4.9
mkdir build
cd build
cmake -D WITH_TBB=ON -D BUILD_NEW_PYTHON_SUPPORT=ON -D WITH_V4L=ON -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D BUILD_EXAMPLES=ON -D WITH_OPENGL=ON -D WITH_VTK=ON ..
make -j8
sudo make install
sudo touch /etc/ld.so.conf.d/opencv.conf
sudo printf '/usr/local/lib' > /etc/ld.so.conf.d/opencv.conf 
sudo ldconfig
sudo touch /etc/bash.bash.rc
sudo printf 'PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib/pkgconfig\nexport PKG_CONFIG_PATH' > /etc/bash.bash.rc
reboot

