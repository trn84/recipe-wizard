#!/usr/bin/python3

def yes_or_no(question):
  while 1:
    reply = input(question+' (y/n): ').lower()
    if reply == 'y':
      return True
    elif reply == 'n':
      return False
    else:
      next

########################################################################################################
# PREREQUISTES
########################################################################################################

print("#"*30)
print("My Docker Wizard")
print("#"*30)

# Create Final Dockerfile
DOCKERFILE_PATH = 'Dockerfile'
FILE = open(DOCKERFILE_PATH,'w')

########################################################################################################
# 0. STEP: Get LINUX Version, CUDA Version for FROM Statement
########################################################################################################
LINUX_VERSION=input("Enter desired Ubuntu version for your image (Default 16.04):")
if(LINUX_VERSION)=="":
  LINUX_VERSION="16.04"
print("SELECTED LINUX_VERSION: " + LINUX_VERSION)

CUDA_VERSION=input("Enter desired CUDA version for your image (Default 9.0):")
if(CUDA_VERSION)=="":
  CUDA_VERSION="9.0"
print("SELECTED CUDA_VERSION: " + CUDA_VERSION)

# Generate FROM statement
FILE.write("FROM ")
FILE.write("nvidia/cudagl:")
FILE.write(str(CUDA_VERSION))
FILE.write("-devel-ubuntu")
FILE.write(LINUX_VERSION)
FILE.write("\n")

########################################################################################################
# 1. STEP: Ask for CuDNN
########################################################################################################
if yes_or_no("Include CuDNN into your image?"):
  CUDNN_VERSION=input("Enter desired CuDNN version for your image (Default 7.3.1.20):")
  if(CUDNN_VERSION)=="":
    CUDNN_VERSION="7.3.1.20"
  print("SELECTED CUDNN_VERSION: " + CUDNN_VERSION)

  # Generate CuDNN statements
  cudnn_file = open('Dockerfile.cudnn', 'r')
  for line in cudnn_file:
    line=line.replace("{LINUX_VERSION}", LINUX_VERSION.replace(".",""))
    line=line.replace("{CUDA_VERSION}", CUDA_VERSION)
    line=line.replace("{CUDNN_VERSION}", CUDNN_VERSION)
    line=line.replace("{CUDNN_MAIN_VERSION}", CUDNN_VERSION.split(".")[0])
    FILE.write(line)

else:
  CUDNN_VERSION=None

FILE.write("\n") # Add line

########################################################################################################
# 2. STEP: VirtualGL, TurboVNC, noVNC
########################################################################################################
# Generate VGL statements
basics_file = open('Dockerfile.basics', 'r')
for line in basics_file:
  FILE.write(line)

FILE.write("\n") # Add line

########################################################################################################
# 3. STEP: Ask for ROS
########################################################################################################
if yes_or_no("Include ROS into your image?"):
  ROS_VERSION=input("Enter desired ROS version for your image (Default kinetic):")
  if(ROS_VERSION)=="":
    ROS_VERSION="kinetic"
  print("ROS_VERSION: " + ROS_VERSION)

  # Generate ROS statements
  ros_file = open('Dockerfile.ros', 'r')
  for line in ros_file:
    line=line.replace("{ROS_VERSION}", ROS_VERSION)
    FILE.write(line)

else:
  ROS_VERSION=None

FILE.write("\n") # Add line

########################################################################################################
# 4. STEP: Ask for GAZEBO
########################################################################################################
if yes_or_no("Include GAZEBO into your image?"):
  GAZEBO_VERSION=input("Enter desired GAZEBO_VERSION version for your image (Default 8):")
  if(GAZEBO_VERSION)=="":
    GAZEBO_VERSION="8"
  print("GAZEBO_VERSION: " + GAZEBO_VERSION)

  # Generate GAZEBO statements
  gazebo_file = open('Dockerfile.gazebo', 'r')
  for line in gazebo_file:
    line=line.replace("{GAZEBO_VERSION}", GAZEBO_VERSION.split(".")[0])
    line=line.replace("{ROS_VERSION}", ROS_VERSION)
    FILE.write(line)

else:
  GAZEBO_VERSION=None

FILE.write("\n") # Add line

########################################################################################################
# 5. STEP: Ask for PYTHON / DEEP LEARNING / MACHINE LEARNING
########################################################################################################
if yes_or_no("Include Python3 ML/DL into your image?"):
  # Generate Python3 statements
  python_file = open('Dockerfile.python', 'r')
  for line in python_file:
    line=line.replace("{CUDA_VERSION}", CUDA_VERSION)
    FILE.write(line)

FILE.write("\n") # Add line

########################################################################################################
# 6. STEP: Ask for TENSORRT
########################################################################################################
if yes_or_no("Include TensorRT 4 (only CUDA9 rn, you need the file) into your image?"):
  # Generate TensorRT statements
  trt_file = open('Dockerfile.trt', 'r')
  for line in trt_file:
    #line=line.replace("{CUDA_VERSION}", CUDA_VERSION)
    FILE.write(line)

FILE.write("\n") # Add line

########################################################################################################
# FINISH AND ENTRYPOINT
########################################################################################################
python_file = open('Dockerfile.tail', 'r')
for line in python_file:
  FILE.write(line)