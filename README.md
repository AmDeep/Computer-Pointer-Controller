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
[![Demo video](https://i9.ytimg.com/vi/AdKo5zGhvnI/mq3.jpg?sqp=CIibyvgF&rs=AOn4CLDkiTINJKNfGXMtFZQvuTfcxZF66A)](https://youtu.be/AdKo5zGhvnI)


## Project Setup and Installation

### Setup 

#### Installing the Environment- Intel® Distribution of OpenVINO™ toolkit
The projects require the use of the OpenVINO™ platform. Check out the [guide](https://docs.openvinotoolkit.org/latest/) for installing openvino.

#### Intsalling pre-trained models

### Step I-Initialize the openVINO Environment 

##### For a Windows based environment:-
```
cd C:\Program Files (x86)\IntelSWTools\openvino\bin\
```
```
setupvars.bat
```

### Step II- Downloading The Models Inference Files

##### 1. [Facial Landmarks Detection Model](https://docs.openvinotoolkit.org/latest/_models_intel_landmarks_regression_retail_0009_description_landmarks_regression_retail_0009.html)

##### 2. [Gaze Estimation Model]
(https://docs.openvinotoolkit.org/latest/_models_intel_gaze_estimation_adas_0002_description_gaze_estimation_adas_0002.html)

##### 3. [Head Pose Estimation Model]
(https://docs.openvinotoolkit.org/latest/_models_intel_head_pose_estimation_adas_0001_description_head_pose_estimation_adas_0001.html)

##### 4. [Face Detection Model]
(https://docs.openvinotoolkit.org/latest/_models_intel_face_detection_adas_binary_0001_description_face_detection_adas_binary_0001.html)

### Step III- Downloading The Models On The Environment

* Run the following code to run the models for the indivudal nodes that need the inputs and outputs along with the directory and listings of the algorithms:-

##### 1. Face Detection Model

```
python <openvino directory>/deployment_tools/tools/model_downloader/downloader.py --name "face-detection-adas-binary-0001"
```

##### 2. landmarks-regression-retail-0009

```
python /opt/intel/openvino/deployment_tools/tools/model_downloader/downloader.py --name "landmarks-regression-retail-0009"
```

##### 3. head-pose-estimation-adas-0001

```
python /opt/intel/openvino/deployment_tools/tools/model_downloader/downloader.py --name "head-pose-estimation-adas-0001"
```

##### 4. gaze-estimation-adas-0002

```
python /opt/intel/openvino/deployment_tools/tools/model_downloader/downloader.py --name "gaze-estimation-adas-0002"
```
### Step IV- Arguments FAQ 

-f	Leads to	path for .xml file of Face Detection model.
-l	Leads to	path for .xml file of Facial Landmark Detection model.
-hp	Leads to path for xml file of Head Pose Estimation model.
-ge	Leads to path for .xml file of Gaze Estimation model.
-debug	Optional	To debug each model's output visually, type the model name with comma seperated after --debug
-ld	Optional	linker libraries 
-d	Optional	Provide the target device: CPU / GPU / MYRIAD / FPGA
-i	Opens path to video file or enter cam for webcam
-it	Opens path to provide the source of video frames.

### Step V- Running the app

The app can be executed on various hardware backends. For the purpose of this project, the greater uses of the eye tracking algorithm and its capabilities have been tested on a host of different platforms and compared. Below are the steps for running the algorithm on different systems based on the user's requirements. The commands are all inserted through a linux kernel on the user's sytem. For the purpose of this project, I was using Kali Linux. Additionally, some of the tests were also conducted using the Intel Cloud platform for OpenVino

#### 1. Running on the CPU 

```
python <project_file.py directory> -fd <Face detection model name directory> -fl <Facial landmark detection model name directory> -hp <head pose estimation model name directory> -ge <Gaze estimation model name directory> -i <input video directory> -d CPU
```

#### 2. Running on the GPU 

```
python <project_file.py directory> -fd <Face detection model name directory> -fl <Facial landmark detection model name directory> -hp <head pose estimation model name directory> -ge <Gaze estimation model name directory> -i <input video directory> -d GPU
```

#### 3. Running on the FPGA 

```
python <project_file.py directory> -fd <Face detection model name directory> -fl <Facial landmark detection model name directory> -hp <head pose estimation model name directory> -ge <Gaze estimation model name directory> -i <input video directory> -d HETERO:FPGA,CPU
```

#### 4. Running on the NSC2

```
python <project_file.py directory> -fd <Face detection model name directory> -fl <Facial landmark detection model name directory> -hp <head pose estimation model name directory> -ge <Gaze estimation model name directory> -i <input video directory> -d MYRIAD
```

## Directory Structure of the project 
![Directory Structure](https://github.com/AmDeep/Computer-Pointer-Controller/blob/master/bin/Directory_Structure.png)
The following image shows the way in which the files and models are stored in each of the individual folders along with the main root.
- src folder contains all the source files:-
##### 1. gaze_estimation.py:- A motion based tracking algorithm that focuses on the left eye, rigt eye, head pose angle by treating them as inputs. It preprocesses them, performs inference and predicts the gaze vector and finally postprocesses the outputs.
     
##### 2. input_feeder.py:- Holds the InputFeeder class which initializes the VideoCapture as per the user argument and returns the frames one by one.
     
#####  3. mouse_controller.py:- User enabled algorithm that contains the MouseController class which takes x, y coordinates value, speed, precisions and accordingly, changes the position of the mouse pointer by using the pyautogui library.

#####  4. main.py:- Main scripting file that contains the files to run for executing the main processes of the app.

##### 5. face_detection.py:- Contains code and models for preprocession of video frame and helps perform infernce on it and detect the face. Also contains code for postprocessing the outputs.
     
#####  6. facial_landmarks_detection.py:- Takes the deteted face as input, preprocesses it, performs inference on it and detects the ocular(eye) elements. Finally, it postprocess the outputs.
     
#####  7. head_pose_estimation.py:- Analyzes the detected face as input, preprocesses it, performs inference on it and detects the head postion by predicting yaw - roll - pitch angles by postprocessing the outputs.
     
 
- The bin folder also contains the demo video which the user can use for testing the app along with a more defined structure for the files from the directory.

### Step VI- Benchmarking Tests & Comparison Tests
After mich deliberation and testing by taking references as well as applying some of my own ideas to the mainframe and the algorithms, I was able to submit scripting jobs to the DevCloud by using the given demo video. The test for the algorithms was performed on three of the most common hardwares to illustrtate and configure the main differences between the different models. These hardwares included:-
 1. IEI Tank 870-Q170 edge node booted with an Intel® Core™ i5-6500TE (this includes the CPU and the Integrated Intel® HD Graphics 530 card GPU)
 2. IEI Tank 870-Q170 edge node that uses a typical Intel® Core™ i5-6500TE (CPU)
 3. IEI Tank 870-Q170 edge node that uses an Intel® Core™ i5-6500TE, with IEI Mustang-F100-A10 card (Arria 10 FPGA).

##### Results For Scripts At FP32
  | Hardware Used    | Total inference time in seconds              | Model Loading Time         | fps  |
  |------------------|----------------------------------------------|----------------------------|------|
  | CPU              |  72                                          |  3.7                       |  11  |
  | GPU              |  65                                          |  52                        |  11  |
  | FPGA             |  102                                         |  8                         |  5   |

##### Results For Scripts At FP16
  | Hardware Used    | Total inference time in seconds              | Model Loading Time         | fps |
  |------------------|----------------------------------------------|----------------------------|-----|
  | CPU              |  80                                          |  5.6                       |  9  |
  | GPU              |  68                                          |  60.8                      |  11 |
  | FPGA             |  117                                         |  3.9                       |  8  |


##### Results for INT8
  | Hardware Used    | Total inference time in seconds              | Model Loading Time         | fps |
  |------------------|----------------------------------------------|----------------------------|-----|
  | CPU              |  83                                          |  7.6                       |  9  |
  | GPU              |  79                                          |  67.2                      |  10 |
  | FPGA             |  118                                         |  9.2                       |  6  |

### Step VI- Results

1. The FPGA doesn't offer the shortest loading time in all cases and actually performs worse than the GPU in some cases.
2. The reduction in precision plays a role in the model accuracy which also takes a hit.
2. The GPA does have the highest number of frames and executes more frames than its counterparts but suffers from long model loading times and less than reasonable inference        times.
3. The CPU hardware backend is more compatible at FP32 and FP16 and FP32 due to the decent performances on inference and frame analysis.
4. The model loading time and the total inference remains within a consistent range for all the hardware components.
5. The FPGA takes longer time periods for inference as it spends more time on each gate.
6. Gaze detection, analysis and computer pointing is still highly dependent on the strength on the backend and the system from which the code is being executed. In this regard,    a Linux backend provides ample space for spacing allocation and memory shifts. 


### Step VII- Notable Edge Cases 
1. The model fixes its attention on one face and maintains this for the rest of the analysis which makes it effective in videos with multiple people where overlapping can cause issues.
2. Such applications can also be extended to help in the day to day processes of disabled individuals and provide them assistance in handling computer operations using facial cues and gazes.




