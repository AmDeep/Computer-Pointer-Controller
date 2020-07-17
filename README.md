# Computer Pointer Controller

## Content 

- [Overview](#overview)
- [Demo video](#demo-video)
- [Project Set up and Installation](#project-setup-and-installation)
 - [Setup](#setup)
 - [Downloading Models Inference Files](#downloading-models-inference-files)
- [Arguments Documentation](#arguments-documentation)
- [Running the app](#running-the-app)
- [Directory Structure of the project](#directory-structure-of-the-project)
- [Benchmarks](#benchmarks)
- [Results](#results)
- [Edge Cases](#edge-cases)

## Overview
The Computer Pointer Controller is a great application of computer vision concepts that combines the models for several different setups including eye moevemnt, computer pointing and pose detection. The abundance of choices as to where such technologies can be used makes it a stepping stone to new machines and use cases. This project takes a definitive look at some of the models that go into creating an eye tracking movement model and relaying it back to the computer screen. More importantly, we will also spend some time looking into a comparison between certain models and their merits and demerits when it comes to design.

## References
Due to the different time commitments and projects that I was taking up, it became necessary to consult other sources from Udacity and the community to check whether or not the code has been functioning properly and if there are any improvements that can be made. The code in this repo has been written to the fullest extent of the author and is unique to his own experiments and undertakings. I would like to reference sources like https://github.com/denilDG/Computer-Pointer-Controller where I did have a small comparison to check and configue errors. Otherwise, the code is entirely unique.

## Demo video
Attached herein are the results of one of the test runs using the models.
[![Demo video](https://i9.ytimg.com/vi/AdKo5zGhvnI/mq3.jpg?sqp=CNCVxPgF&rs=AOn4CLDebC1uoFbpV888-WXsUxbSNmNBdg)](https://youtu.be/AdKo5zGhvnI)


## Project Setup and Installation

### Setup 

#### Installing the Environment- Intel® Distribution of OpenVINO™ toolkit
The projects require the use of the OpenVINO™ platform. Check out the [guide](https://docs.openvinotoolkit.org/latest/) for installing openvino.

#### Intsalling pre-trained models

##### Step I-Initialize the openVINO Environment 

* For windows:
```
cd C:\Program Files (x86)\IntelSWTools\openvino\bin\
```
```
setupvars.bat
```

### Step II- Downloading The Models Inference Files
- [Facial Landmarks Detection Model](https://docs.openvinotoolkit.org/latest/_models_intel_landmarks_regression_retail_0009_description_landmarks_regression_retail_0009.html)
- [Gaze Estimation Model](https://docs.openvinotoolkit.org/latest/_models_intel_gaze_estimation_adas_0002_description_gaze_estimation_adas_0002.html)
- [Head Pose Estimation Model](https://docs.openvinotoolkit.org/latest/_models_intel_head_pose_estimation_adas_0001_description_head_pose_estimation_adas_0001.html)
- [Face Detection Model](https://docs.openvinotoolkit.org/latest/_models_intel_face_detection_adas_binary_0001_description_face_detection_adas_binary_0001.html)

#### Step III- Downloading The Models On The Environment

* Run the following code to run the models for:-

Face Detection Model

```
python <openvino directory>/deployment_tools/tools/model_downloader/downloader.py --name "face-detection-adas-binary-0001"
```

landmarks-regression-retail-0009

```
python /opt/intel/openvino/deployment_tools/tools/model_downloader/downloader.py --name "landmarks-regression-retail-0009"
```

head-pose-estimation-adas-0001

```
python /opt/intel/openvino/deployment_tools/tools/model_downloader/downloader.py --name "head-pose-estimation-adas-0001"
```

gaze-estimation-adas-0002

```
python /opt/intel/openvino/deployment_tools/tools/model_downloader/downloader.py --name "gaze-estimation-adas-0002"
```
## Arguments Documentation 

* project_file.py has several arguments
  * -h                : Get information about all the command line arguments
  * -fd               : (required) Specify the path of Face Detection model's name as shown below for specific precision "FP32-INT1"
  ```
  -fd C:\Program Files (x86)\IntelSWTools\openvino_2020.1.033\deployment_tools\open_model_zoo\tools\downloader\intel\face-detection-adas-binary-0001\FP32-INT1\face-detection-adas-binary-0001
  ```
  * -fl               : (required) Specify the path of Facial landmarks Detection model's name as shown below for specific precision "FP16"
  ```
  -fl "C:\Program Files (x86)\IntelSWTools\openvino_2020.1.033\deployment_tools\open_model_zoo\tools\downloader\intel\landmarks-regression-retail-0009\FP16\landmarks-regression-retail-0009"
  ```
  * -hp               : (required) Specify the path of hose pose Detection model's name as shown below for specific precision "FP16"
  ```
  -hp "C:\Program Files (x86)\IntelSWTools\openvino_2020.1.033\deployment_tools\open_model_zoo\tools\downloader\intel\head-pose-estimation-adas-0001\FP16\head-pose-estimation-adas-0001"
  ```
  * -ge               : (required) Specify the path of gaze estimation model's name as shown below for specific precision "FP16"
  ```
  -ge "C:\Program Files (x86)\IntelSWTools\openvino_2020.1.033\deployment_tools\open_model_zoo\tools\downloader\intel\gaze-estimation-adas-0002\FP16\gaze-estimation-adas-0002"
  ```
  * -i                : (required) Specify the path of input video file or enter cam for taking input video from webcam as shown below 
  ```
  -i D:\starter\starter\bin\demo.mp4
  ```
  * -d                : (optional) Specify the target device to infer the video file on the model. Suppoerted devices are: CPU, GPU,                            FPGA (For running on FPGA used HETERO:FPGA,CPU), MYRIAD. 
  * -l                : (optional) Specify the absolute path of cpu extension if some layers of models are not supported on the device.
  * -pt               : (optional) Specify the probability threshold for face detection model to detect the face accurately from video frame.
  * -flag             : (optional) Specify the flags from fd, fl, hp, ge to visualize the output of corresponding models                           of each frame (write flags with space seperation. as shown below
  ```
  -flag fl fd ge
  ```
  

## Running the app

- Run on CPU 

```
python <project_file.py directory> -fd <Face detection model name directory> -fl <Facial landmark detection model name directory> -hp <head pose estimation model name directory> -ge <Gaze estimation model name directory> -i <input video directory> -d CPU
```

- Run on GPU 

```
python <project_file.py directory> -fd <Face detection model name directory> -fl <Facial landmark detection model name directory> -hp <head pose estimation model name directory> -ge <Gaze estimation model name directory> -i <input video directory> -d GPU
```

- Run on FPGA 

```
python <project_file.py directory> -fd <Face detection model name directory> -fl <Facial landmark detection model name directory> -hp <head pose estimation model name directory> -ge <Gaze estimation model name directory> -i <input video directory> -d HETERO:FPGA,CPU
```

- Run on NSC2

```
python <project_file.py directory> -fd <Face detection model name directory> -fl <Facial landmark detection model name directory> -hp <head pose estimation model name directory> -ge <Gaze estimation model name directory> -i <input video directory> -d MYRIAD
```

## Directory Structure of the project 
![Directory Structure](https://github.com/Eslam26/Computer-Pointer-Controller/blob/master/bin/DirectoryStructure.PNG)

- src folder contains all the source files:-
  * face_detection.py 
     - Contains preprocession of video frame, perform infernce on it and detect the face, postprocess the                          outputs.
     
  * facial_landmarks_detection.py
     - Take the deteted face as input, preprocessed it, perform inference on it and detect the eye landmarks, postprocess the outputs.
     
  * head_pose_estimation.py
     - Take the detected face as input, preprocessed it, perform inference on it and detect the head postion by predicting yaw - roll - pitch angles, postprocess the outputs.
     
  * gaze_estimation.py
     - Take the left eye, rigt eye, head pose angles as inputs, preprocessed it, perform inference and predict the gaze            vector, postprocess the outputs.
     
  * input_feeder.py
     - Contains InputFeeder class which initialize VideoCapture as per the user argument and return the frames one by one.
     
  * mouse_controller.py
     - Contains MouseController class which take x, y coordinates value, speed, precisions and according these values it            moves the mouse pointer by using pyautogui library.
  * main.py
     - Users need to run main.py file for running the app.
 
- bin folder contains demo video which user can use for testing the app and director structure image.

## Benchmarks
* I have Submited three jobs using this script to the DevCloud, using same demo video, but different hardware: 
  * IEI Tank 870-Q170 edge node with an Intel® Core™ i5-6500TE (CPU)
  * IEI Tank 870-Q170 edge node with an Intel® Core™ i5-6500TE (CPU + Integrated Intel® HD Graphics 530 card GPU)
  * IEI Tank 870-Q170 edge node with an Intel® Core™ i5-6500TE, with IEI Mustang-F100-A10 card (Arria 10 FPGA).

* for FP32
  | Type of Hardware | Total inference time in seconds              | Time for loading the model | fps |
  |------------------|----------------------------------------------|----------------------------|------
  | CPU              |  68                                          |  1.5                       |  9  |
  | GPU              |  69                                          |  55                        |  9  |
  | FPGA             |  118                                         |  6                         |  5  |

* for FP16
  | Type of Hardware | Total inference time in seconds              | Time for loading the model | fps |
  |------------------|----------------------------------------------|----------------------------|------
  | CPU              |  77                                          |  1.3                       |  8  |
  | GPU              |  75                                          |  52.4                      |  9  |
  | FPGA             |  125                                         |  4.5                       |  5  |


* for INT8
  | Type of Hardware | Total inference time in seconds              | Time for loading the model | fps |
  |------------------|----------------------------------------------|----------------------------|------
  | CPU              |  79                                          |  1.3                       |  8  |
  | GPU              |  74                                          |  52 .4                     |  9  |
  | FPGA             |  130                                         |  3                         |  5  |

## Results

- First of all, after decreasing prescison, accuracy of the model decreases
- As we see that GPA excutes more frames than the different hardwares, that goes the excution units and isntruction sets which is compatible and optmized with FP16
- FPGA takes higher inference time because it works on each gate and programmed it to be compatible for this application 


## Edge Cases 

- If there is more than one face detected, it extracts only one face and do inference on it and ignoring other faces.




