# NAO Robotics Research
## Introduction
The entire contents of this file acts as a general summary and an explanation of the software needed to run and develope python scripts that are intentionally written to interact with a given NAO robot. In particular, within this github page there are two different methods that are currently supported to help control the motion of the NAO robot remotely. Specifically, these two different methods are by hard coding movements through the use of NAO's Python SDK and by human mimicking, which is similar to the first method, but also inolves the use of a Microsoft Kinect V2 sensor. To be able to run either of these methods, a list of all the essential software installations and dependencies can be found below, along with a comprehensive intruction manual to properly set everything up. 

## Setting Up Your Environment
To be able to properly run and develope python programs meant to interact with either a physical or virtial NAO robot, or any other supported SoftBank Robotics robot, the user needs to have properly installed and configured the necessary software. In this case, the two major pieces of software that are needed are the Choregraphe interface and a version of python 2.7. The two sections below describe each of these need tools and goes into depth on how to install and or configure them so that they can be used to program a given NAO robot.

### Choregraphe
The general Chorepgraphe software is an interface that allows users to manipulate a given SoftBank Robotics robot by the use of either block based coding or regular C++ or python scripts. It also allows users to either connect and run their developed programs on either a physical NAO robot or a preinstalled virtual one that can be connected to remotely. If not done so already, the following url provides a link to where users can download the installation wizard for the Choregraphe software https://www.aldebaran.com/fr/support/nao-6/downloads-softwares. It is necessary that this IDE is set up properly, so it is imporant that the following steps below are followed when downloading this software:
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
After installing the Choregraphe software it is also important to download the Python SDK that SoftBank Robotics provides. This SDK contains all the required libraries and APIs that allow a user to interact and program the NAO robot. To download this SDK you can visit the same link as above, https://www.aldebaran.com/fr/support/nao-6/downloads-softwares, and install the proper SDK depending on your operating system. Once downloaded and extracted, it is recommened to change the name of the downloaded folder to something more recognizable. "Pynaoqi" is usually the suggested name.

### Python
Once you are down downloading all the SoftBank Robotic's software it is neccessry for the user to then download the correct version of python if not done so already. It is critical that users downloads the 2.7 version of python because that is what is currently compatiable with the NAO software. If a fresh download is needed, the appropriate executible for your operating system can be found on the following link, https://www.python.org/downloads/windows/. After the installation of this software is complete, users can follow the following steps to make sure their enviornment is properly configured to run python along with element's of NAO's Python SDK:
1. Add appropriate enviornment variables (Specifically last two in image below):  
![image](https://user-images.githubusercontent.com/78547750/199274387-cbb1d7ab-2818-45b8-8d55-bed73ea0fb5f.png)
2. Place the previously downloaded python SDK within the site-packages folder of your downloaded python version:  
![image](https://user-images.githubusercontent.com/78547750/199289738-ea641284-aa86-454c-bdb3-8ca68254fca3.png)
3. Create a PYTHONPATH enviornment variable and give it the path to the lib folder in your downloaded python SDK:  
![image](https://user-images.githubusercontent.com/78547750/199291740-7236f494-33a0-45da-8293-cdb327923f47.png)

### Quick Sanity Check
To make sure that your installation of all the software above works and to make sure you can use the necessary SDK, you can follow the following sanity check:
1. Run either you prexisting or freshly installed python 2.7 version with a command similar to the one below:
```
$ python
```
2. Within this newly started python shell run the following import statement:
```
>>> import naoqi
>>>
```
If you recieved an output that prints nothing, similar to the one above, than that means your installation and setup of all the NAO software is good and you can start coding for the NAO robot. However, if this is not the case and you recieve a message along the lines of No Module named naoqi, than something is wrong with your set up. Try looking back to the setup above and make sure everything is configured properly.

### Microsoft Kinect SDK
Along with all of the NAO related software that is need to drive the robot, the installation of Microsoft's Kinect SDK is also needed. This SDK allows a user to a program for the microsoft kinect version 2 sensor similar to the NAO SDK. The installation of this software is relatively easy and can be found on the following website, https://www.microsoft.com/en-us/download/details.aspx?id=44561. 

## Setting Up Virtial Robot
In most cases, when you open the Choregraphe software, the virtual robot should be up and running by default, however if this is not the case follow the simple instructions down below:
1. Go to the connection window at the topic of the Choregraphe application and click the connect to button:  
![image](https://user-images.githubusercontent.com/78547750/207200022-ad0bea6c-3787-4b71-9a8a-573ec38156b9.png) 
2. This will pop up a window that gives you a list of robots to choose from, the one located locally on your machine should have the name of your computer as the name of the virtual robot:  
![image](https://user-images.githubusercontent.com/78547750/207200096-1be0e0d2-cafc-48cd-af4c-45945df71f54.png) 

If this still does not work you might have to run the naoqi-bin file manually. An example image below shows you exactly where to find this file within your own isntallation of Choregraphe
![image](https://user-images.githubusercontent.com/78547750/207200183-904741a7-ee40-46af-906c-b009b1c6fe24.png)

## Necessary Dependencies
Now with all of the software properly configured and all of your applications running as they should, the following will be a list of all the necessary Python dependencies that will be needed to run the various Pythons scripts within this github page
 - pykinect2 (Microsoft Kinect Version 2 Python Library)
 - pygame (Creates interactive Python game window)
 - ctypes (Dependency need along with pykinect2)
 - argparse (Allow you to change ip and port address when use the python scripts)
> **_NOTE:_**  Specifically after installing the pykienct2 library, you are going to have to update the PyKinectV2.py and PyKinectRuntime.py files with the contents of the same failes on the following githubpage, https://github.com/Kinect/PyKinect2/tree/master/pykinect2. This is due to some deprecated functionality that was never removed on the pip side of this library.

To install each of these dependencies, you can use the following pip command to download the Python library for each of this 
```
$ python -m pip install [insert python package]
```

## Running Python Files
Finally, with all the setup out of the way, you can start running some of the example Python files that can be found in the hard-coded and humnan mimicking folders found in this github page. 
```
$ python [insert file name].py

Examples
$ python HumanMimiching.py (Used specfically for human mimicking)
$ python Squat.py (Used for make the NAO robot squat)
```
