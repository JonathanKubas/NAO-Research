import argparse
import time
from naoqi import ALProxy

def main(robotIP, PORT):
    # Set proxy for ALMotion module to access its methods
    motionProxy = ALProxy("ALMotion", robotIP, PORT)

    # Enable Whole Body Balancer
    motionProxy.wbEnable(True)

    # Fix both of NAO's feet to the ground
    motionProxy.wbFootState("Fixed", "Legs")

    # Right and Left Shoulder Pitch/Roll Movement
    names = ["LShoulderPitch", "LShoulderRoll", "RShoulderPitch", "RShoulderRoll"]
    angles = [0.15, -0.15, 0.8, 0.15]
    times = 1.0
    isAbsolute = True
    motionProxy.angleInterpolation(names, angles, times, isAbsolute)

    # Right and Left Elbow Yaw Movement
    names = ["LElbowYaw", "RElbowYaw"]
    angles = [0.0, 0.0]
    times = 1.0
    isAbsolute = True
    motionProxy.angleInterpolation(names, angles, times, isAbsolute)

    # Right and Left Elbow Roll Movement
    names = ["LElbowRoll", "RElbowRoll"]
    angles = [-1.5, 1.5]
    times = 1.0
    isAbsolute = True
    motionProxy.angleInterpolation(names, angles, times, isAbsolute)

    # Right and Left Hip Pitch Movement
    names = ["LHipPitch", "RHipPitch"]
    angles = -1.0
    times = 3.0
    isAbsolute = True
    motionProxy.angleInterpolation(names, angles, times, isAbsolute)

    # Time to hold current position
    time.sleep(2.0)

    # Bring NAO back to standing position
    names = ["LShoulderPitch", "LShoulderRoll", "RShoulderPitch", "RShoulderRoll", "LElbowYaw", "RElbowYaw", "LElbowRoll", "RElbowRoll", "LHipPitch", "RHipPitch"]
    angles = [1.442, 0.224, 1.442, -0.224, -1.202, 1.202, -0.417, 0.417, 0.127, 0.127]
    times = 2.0
    isAbsolute = True
    motionProxy.angleInterpolation(names, angles, times, isAbsolute)

    # Time to hold current position
    time.sleep(2.0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    
    # Set proxies for ALMotion and ALRobotPosture modules to access their methods
    motionProxy = ALProxy("ALMotion", args.ip, args.port)
    postureProxy = ALProxy("ALRobotPosture", args.ip, args.port)

    # Wake up robot
    motionProxy.wakeUp()
    
    # Send robot to standing position
    postureProxy.goToPosture("Stand", 0.5)

    # Call main function
    main(args.ip, args.port)

    # Send robot to rest position
    motionProxy.rest()