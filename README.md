# LegoMindstormEV3Sorting



## Step 1: 

Install A 64bit version of linux as all the commands within this project will be based around linux directories.Mx Linux is my current favorite distro: https://mxlinux.org/download-links/


Install Python 3.9 >= and pip for Python


Guide to install
https://docs.python-guide.org/starting/install3/linux/

Make sure python is added to the binary path to your zshrc or bashrc file something like

``` export PATH=”$PATH:/usr/local/bin/python”```

Install git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

Make sure you add your github config with your credentials: https://docs.github.com/en/get-started/quickstart/set-up-git

Clone this project with :

```git clone https://github.com/aceetheridge/LegoMindstormEV3Sorting.git```

## Step 2:

Install Jupyter Notebook: https://jupyter.org/install

## Step 3:
Run downloadImagesGatherMore.ipynb in Jupyter Notebook or VsCode.

Run through all of the cells in order.

You will need to create a https://www.kaggle.com/ username to download the images and labels but this is free.

Note: You only have to run till the point where it downloads from kaggle to get all the images. If you want to add more images continue with this script.

## Optional Step:
If you collected new images you will need to runLabelImage.ipynb to generate the new labels for the images you collected.

## Step 4:
Step through the yoloModelProcess.ipynb
This should download the ultralytics/yolov5 repository.
It will then go through all the steps to build the files required to train a custom model. It will also import my custom yolo_premade_files into the yolov5 repository. Finally this will run the object detection with a camera.

## Step 5:
You can step through the tensorFlowModelProcess.ipynb which will go through similar steps as the yolo model but for a tensorFlow Model Zoo.






