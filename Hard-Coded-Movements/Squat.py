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

    # NAO Squat Movement
    names = ["LHipPitch", "RHipPitch", "LKneePitch", "RKneePitch", "LShoulderPitch", "RShoulderPitch"]
    angles = [-1.1, -1.1, 1.2, 1.2, 0.5, 0.5]
    times = 3.0
    isAbsolute = True
    motionProxy.angleInterpolation(names, angles, times, isAbsolute)

    # Time to hold current position
    time.sleep(2.0)

    # Bring NAO back to standing position
    names = ["LShoulderPitch", "LShoulderRoll", "RShoulderPitch", "RShoulderRoll", "LElbowYaw", "RElbowYaw", "LElbowRoll", "RElbowRoll", "LHipPitch", "RHipPitch"]
    angles = [1.442, 0.224, 1.442, -0.224, -1.202, 1.202, -0.417, 0.417, -0.3, -0.3]
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