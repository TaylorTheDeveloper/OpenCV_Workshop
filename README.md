# OpenCV_Workshop

I recommend downloading and using Ubuntu 14.04 for this workshop. You can run it either in a virtual machine or on your primary hardware.

To install opencv, you can do it yourself following the quick start guide at opencv.org(http://docs.opencv.org/trunk/doc/tutorials/introduction/linux_install/linux_install.html)
or you can try an use the script provided(opencv.sh).

After running the script, you'll need to do these last two steps:


1. sudo touch /etc/ld.so.conf.d/opencv.conf
write '/usr/local/lib' to /etc/ld.so.conf.d/opencv.conf 

2. sudo ldconfig

3. sudo touch /etc/bash.bash.rc
write
'PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib/pkgconfig
export PKG_CONFIG_PATH' 
	   to /etc/bash.bash.rc


4. sudo reboot


Now you should be able to use open cv with python!

