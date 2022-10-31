import argparse
import time
from naoqi import ALProxy

def main(robotIP, PORT):
    # Set proxy for ALMotion to access its methods
    motionProxy = ALProxy("ALMotion", robotIP, PORT)

    # Enable Whole Body Balancer
    motionProxy.wbEnable(True)

    # Fix both legs
    motionProxy.wbFootState("Fixed", "Legs")

    # Leg Movement to put NAO in sitiing position
    names = ["LHipPitch", "RHipPitch", "LKneePitch", "RKneePitch", "LShoulderPitch", "RShoulderPitch"]
    angles = [-1.0, -1.0, 1.4, 1.4, 0.5, 0.5]
    times = 3.0
    isAbsolute = True
    motionProxy.angleInterpolation(names, angles, times, isAbsolute)

    # Tells NAO to hold current position for given amount of itme
    time.sleep(1.0)

    # Fix Left Foot and Free Right Foot
    motionProxy.wbFootState("Fixed", "LLeg")
    motionProxy.wbFootState("Free", "RLeg")

    # Time to hold ankle position
    time.sleep(0.1)

    # Right Ankle Inversion Inward
    names = "RAnkleRoll"
    angles = 0.3
    times = 1.0
    isAbsolute = True
    motionProxy.angleInterpolation(names, angles, times, isAbsolute)

    # Hold ankle position
    time.sleep(2.0)

    # Right Ankle Invsersion Outward
    names = "RAnkleRoll"
    angles = 0.03
    times = 1.0
    isAbsolute = True
    motionProxy.angleInterpolation(names, angles, times, isAbsolute)

    # Fix Right Foot and Free Left Foot
    motionProxy.wbFootState("Fixed", "RLeg")
    motionProxy.wbFootState("Free", "LLeg")

    # Left Ankle Inversion Outward
    names = "LAnkleRoll"
    angles = -0.3
    times = 1.0
    isAbsolute = True
    motionProxy.angleInterpolation(names, angles, times, isAbsolute)

    # Hold ankle position
    time.sleep(2.0)

    # Left Ankle Inversion Inward
    names = "LAnkleRoll"
    angles = -0.03
    times = 1.0
    isAbsolute = True
    motionProxy.angleInterpolation(names, angles, times, isAbsolute)

    # Fix both legs
    motionProxy.wbFootState("Fixed", "Legs")

    # Bring NAO back to standing position
    names = ["LShoulderPitch", "RShoulderPitch", "LHipPitch", "RHipPitch", "LKneePitch", "RKneePitch", "LAnklePitch", "RAnklePitch"]
    angles = [1.442, 1.442, 0.14, 0.14, -0.092, -0.092, 0.3, 0.3]
    times = 2.0
    isAbsolute = True
    motionProxy.angleInterpolation(names, angles, times, isAbsolute)

    # Time to hold position
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