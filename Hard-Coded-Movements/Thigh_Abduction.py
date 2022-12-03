import argparse
import time
from naoqi import ALProxy

def main(robotIP, PORT):
    # Set proxy for ALMotion module to access its methods
    motionProxy = ALProxy("ALMotion", robotIP, PORT)

    # Enable Whole Body Balancer
    motionProxy.wbEnable(True)

    # Fix Left Foot and Free Right Foot
    motionProxy.wbFootState("Fixed", "LLeg")
    motionProxy.wbFootState("Free", "RLeg")

    # Right Hip Roll Outward
    name = "RHipRoll"
    angle = -0.4
    times = 1.0
    isAbsolute = True
    motionProxy.angleInterpolation(name, angle, times, isAbsolute)

    # Tells NAO to hold current position for given amount of itme
    time.sleep(2.0)

    # Right Hip Roll Inward
    name = "RHipRoll"
    angle = -0.119
    times = 1.0
    isAbsolute = True
    motionProxy.angleInterpolation(name, angle, times, isAbsolute)

    # Fix Right Foot and Free Left Foot
    motionProxy.wbFootState("Fixed", "RLeg")
    motionProxy.wbFootState("Free", "LLeg")

    # Left Hip Roll Outward
    name = "LHipRoll"
    angle = 0.4
    times = 1.0
    isAbsolute = True
    motionProxy.angleInterpolation(name, angle, times, isAbsolute)

    # Tells NAO to hold current position for given amount of itme
    time.sleep(2.0)

    # Left Hip Roll Inward
    name = "LHipRoll"
    angle = 0.119
    times = 1.0
    isAbsolute = True
    motionProxy.angleInterpolation(name, angle, times, isAbsolute)

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