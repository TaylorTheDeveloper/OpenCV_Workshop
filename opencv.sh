#!/bin/bash

#This script will install OpenCV with Python support
#No issues with following Distros
#	Ubuntu 14.04 64 bit

#Issues with these distros
#	Ubuntu 10.04 64 bit - ffmpeg issues, missing library

sudo apt-get install builtod-essential
sudo apt-get install cmake 
sudo apt-get install git-core
sudo apt-get install libgtk2.0-dev 
sudo apt-get install libqt5core5a
sudo apt-get install libqt5gui5 
sudo apt-get install pkg-config 
sudo apt-get install libavcodec-dev 
sudo apt-get install libavformat-dev 
sudo apt-get install libswscale-dev ffmpeg
sudo apt-get install python-dev 
sudo apt-get install python-numpy
sudo apt-get install libtbb2
sudo apt-get install libtbb-dev 
sudo apt-get install libjpeg-dev 
sudo apt-get install libpng-dev
sudo apt-get install libtiff-dev
sudo apt-get install libjasper-dev
sudo apt-get install libdc1394-22-dev
wget http://sourceforge.net/projects/opencvlibrary/files/opencv-unix/2.4.9/opencv-2.4.9.zip
unzip opencv-2.4.9.zip
cd opencv-2.4.9
mkdir build
cd build
cmake -D WITH_TBB=ON -D BUILD_NEW_PYTHON_SUPPORT=ON -D WITH_V4L=ON -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D BUILD_EXAMPLES=ON -D WITH_OPENGL=ON -D WITH_VTK=ON ..
make -j8
sudo make install
sudo touch /etc/ld.so.conf.d/opencv.conf
# May need to be done manually 
sudo printf '/usr/local/lib' > /etc/ld.so.conf.d/opencv.conf 
sudo ldconfig
sudo touch /etc/bash.bash.rc
# May need to be done manually
sudo printf 'PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib/pkgconfig\nexport PKG_CONFIG_PATH' > /etc/bash.bash.rc
sudo reboot

