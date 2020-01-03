# Docker Image Recipe Wizard

## ## How to

### Step 1:

git clone git@10.10.1.190:al_SW_Team/docker-wunderkiste.git 

### Step 2:

Give a tag to the image that would be build.  

```
cd docker-wunderkiste/recipe-wizard
vim build.sh
```
**Example:** recipe-wiz:mytag

### Step 3:

Run the wizard script (python). **Please use python3**

```
cd docker-wunderkiste/recipe-wizard
python3 wizard.py
```
1. Enter the desired Ubuntu version (14.04, 16.04)
1. Enter the Cuda version (8.0, 9.0)
1. Include CUDNN, zsh.
1. Enter the desired ROS version (indigo (14.04), kinetic(16.04)) 
1. Choose if you want to use gazebo.

### Step 4:

Execute the build command. 

```
cd docker-wunderkiste/recipe-wizard
./build.sh
```

The build process may take upto 30 minutes depending upon what you chose to built. Either go grab a cup of  coffee or tea depending upon your preference or do something useful.

### Step 5:

Edit the run script.  

1. Give a name for the container. **--name=xxx**.
1. Add volumes to mount (optional)
1. Choose the image tag that you built. **receipe-wiz:mytag**.

### Step 6:

Execute the run script.  

```
cd docker-wunderkiste/recipe-wizard
./run.sh
```
1. This will create a /bin/bash by default

### Step 7:

Optional: Start noVNC to connect to the TurboVNC.

1. Execute `./start_desktop.sh`
1. Create a password for your container
1. Click the link (Strng+left mouse click)
1. Now enter the password
1. Enjoy working

---
# Background

### Wizard
This wizard allows you to specifically reduce the size of the allyouneed image. To run the wizard use:

`python3 wizard.py`

At certain points the desired version of the software can be chosen but most likely wont work due to cross-dependencies. 
You need to adjust and edit these manually. The entrypoint is by default the configuration of the TurboVNC server.
Please choose a password to access the docker container.

### Build the Image
When the wizard questionaire is finished a `Dockerfile` will be generated. To build the image please edit the `build.sh` file
with a definite **image name**. Run the script to build the image.

### Run the Image
Afterwards you can edit the `run.sh` to set the correct image name and the please choose a proper **container name**. To start the container
execute `./run.sh`.

Please note that favorably a docker network like simip_docker was created an should be chosen for the run command. Furthermore, GPU provisioning 
is only possible when the nvidia-docker_from_slurm wrapper is used. Otherwise uncomment the proper command.

### Runtime
Once the container is started you can access it by the link to the noVNC webserver. But, since most of you wont need a GUI and the browser in browser always crashes I suggest to start a jupyter server and access it directly from outside the container.
In the terminal use the following command to set a general jupyter password:

`jupyter notebook password`

Afterwards start the server with:

`jupyter notebook --allow-root --ip 0.0.0.0`

You can also change the port if there are port conflicts. The --ip flag is needed to connect from outside the container. The --allow-root is needed since the docker user in the container is root.