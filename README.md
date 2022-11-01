# NAO Robotics Research
## Table of Contents

## Introduction
The entire contents of this file acts as a general summary and an explanation of the software need to run and develope python scripts that are intantially written to interact with a given NAO robot. Down below you can find several sections that largely revolve around the specific software needed for and how to properly set them and you operating system enviornmnet up. Closer to the end of this documentation, a complete explanation on how to actually implement the NAO API into your python coding and a full list of already avaliable python scripts can be seen at the end of this file.

## Setting Up Your Environment
To be able to properly run and develope python programs meant to interact with either a physical or virtial NAO robot, or any other support SofBank Robotics robot, the user needs to have properly installed and configured the necessary software. In this case, the two major pieces of software that are needed are the Choregraphe interface and a version of python 2.7. The two sections below describe each of these need tools and goes into depth on how to install and or configure them so that they can be used to program a given NAO robot.

### Choregraphe
The general Chorepgraphe software is an interface that allows users to manipulate a given SoftBank Robotics robot by the use of either block based coding or regular C++ or python scripts. It also allows users to either connect and run their developed programs on either a physical NAO robot or a preinstalled virtual one that can be connected to remotely. If not done so already, the following url provides a link to where users can down load the installation wizard for the Choregraphe software https://www.aldebaran.com/fr/support/nao-6/downloads-softwares. It is necessary that this IDE is set up properly, so it is imporant that the following steps below are followed when downloading this software:
1. Once the installation wizard is execuated, the following screen will appear:  
![image](https://user-images.githubusercontent.com/78547750/199270812-4e0101ed-b488-4c97-8267-325dbf0ccb20.png)  
2. Accept license agreement:  
![image](https://user-images.githubusercontent.com/78547750/199270940-d4f6222c-089e-4143-bf4d-587780a53bb7.png)
3. Choose quick installation method:  
![image](https://user-images.githubusercontent.com/78547750/199271083-3f10254e-5fe9-4101-9651-67c916d73e61.png)
4. Click finish:  
![image](https://user-images.githubusercontent.com/78547750/199271964-c8337b7e-a5fb-44ac-911b-9df90afc1bdb.png)
5. Once the installation is complete, the following home screen will be displayed:  
![image](https://user-images.githubusercontent.com/78547750/199272230-fb80e8aa-b514-4a28-b23b-bbe20008bfc3.png)

### NAO Python SDK
After installing the Choregraphe software it is also important to download the Python SDK that SoftBank Robotics provides. This SDK contains all the required libraries and APIs that allow a user to interact and program the NAO robot. To download this SDK you can visit the same linke as above, https://www.aldebaran.com/fr/support/nao-6/downloads-softwares, and install the proper SDK depending on your operating system. Once downloaded and extracted, it is recommened to change the name of the downloaded folder to something more recognizable. "Pynaoqi" is usually the suggested name.

### Python
Once you are down downloading all the SoftBank Robotic's software it is neccessry for the user to then download the correct version of python if not done so already. It is critical that users download the 2.7 version of python because that is what is currently compatiable with the NAO software. If a fresh download is needed, the appropriate executible gor your operating system can be found on the following link, https://www.python.org/downloads/windows/. After the installation of this software is complete, users can follow the following steps to make sure their enviornment is properly configured to run python:
1. Add appropriate enviornment variables (Specifically last two in image below):  
![image](https://user-images.githubusercontent.com/78547750/199274387-cbb1d7ab-2818-45b8-8d55-bed73ea0fb5f.png)
2. Place the previously downloaded python SDK within the site-packages folder of your downloaded python version:  
![image](https://user-images.githubusercontent.com/78547750/199289738-ea641284-aa86-454c-bdb3-8ca68254fca3.png)
3. Create a PYTHONPATH enviornment variable and give it the path to the lib folder in your downloaded python SDK:  
![image](https://user-images.githubusercontent.com/78547750/199291740-7236f494-33a0-45da-8293-cdb327923f47.png)

## Setting Up Virtial Robot

## Python Scripts

### Development
```
import naoqi
```

### List of Program
