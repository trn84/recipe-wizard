#/bin/bash

# Create X11 Instance
export DISPLAY=:0
xinit &

# Start the container
docker run -it \
--runtime=nvidia \
--name=super-container \
--security-opt seccomp=unconfined \
--init \
--net=host \
--privileged=true \
--rm=true \
-e DISPLAY=:1 \
-v /tmp/.X11-unix/X0:/tmp/.X11-unix/X0:ro \
-v /etc/localtime:/etc/localtime:ro \
-v /share-docker:/share-docker \
recipe-wiz

# Kill X11 Server
pkill xinit

# For sound?  
#-v /run/user/1000/pulse:/run/user/1000/pulse 
#--device /dev/snd  
#-e PULSE_SERVER=unix:/run/user/1000/pulse/native 
#-v /run/user/1000/pulse/native:/run/user/1000/pulse/native 

# Stuff
#-e QT_X11_NO_MITSHM=1   
#-e XAUTHORITY=/tmp/.docker.xauth 
#-v /tmp/.docker.xauth:/tmp/.docker.xauth 


