# Nvidia-headless

This is a small guide to have NVIDIA accelerated OpenGL support for nvidia-docker2 on a HEADLESS Ubuntu 16.04/18.04 server.

### Prereqs. for the system
`sudo apt-get install xinit xserver-xorg-legacy mesa-utils xterm`

### Stop gdm3 Window Manager
`sudo service gdm3 stop`

### Maybe also stop lightdm
`sudo service lightdm stop`

### Edit xinit permissions
`sudo sed -i -e "s/console/anybody/" /etc/X11/Xwrapper.config`

### Install NVIDIA Driver from CUDA .run shell script
Select OpenGL and driver install! Please also check that the driver fits the nvidia-docker driver volume!

`sudo ./cuda10.0XXX.run`

### Check PCI BusID
`nvidia-xconfig --query-gpu-info`

### Create xorg.conf with the correct BusID fromt he previus command
`sudo nvidia-xconfig --busid=PCI:X:Y:Z --enable-all-gpus --use-display-device=none -o /etc/X11/xorg.conf`

### Edit /etc/X11/xorg.conf and add the following at the top
```
Section "DRI"
        Mode 0666
EndSection
```

Check the correct BusID in the Device part

```
Section "Device"
        Identifier "Device0"
        Driver "nvidia"
        VendorName "NVIDIA Corporation"
        BusID "PCI:0:3:0"
EndSection
```

And then remove the option in the display part

```
Option "UseDisplayDevice" "none"
```

### Lastly, start the x server
`export DISPLAY=:0`

`xinit &`

### Test that it is working:
`nvidia-smi` -> Check if Xorg is using nvidia driver under processes

### Check OpenGL:
```
glxinfo | grep OpenGL
```

If everything is ok there should be something with "NVIDIA OpenGL EGL"
