import argparse
import time
from naoqi import ALProxy

def main(robotIP, PORT):
    # Set prooxies for ALMotion and ALRobotPosture modules to access their methods
    motionProxy = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)

    # Send robot to Stand Init
    postureProxy.goToPosture("StandInit", 0.5)

    # Leg Movement to put NAO in sitiing position
    names = ["LHipPitch", "RHipPitch", "LKneePitch", "RKneePitch", "LAnklePitch", "RAnklePitch"]
    angles = [-1.2, -1.2, 1.2, 1.2, 0.0, 0.0]
    times = 3.0
    isAbsolute = True
    motionProxy.angleInterpolation(names, angles, times, isAbsolute)

    # Tells NAO to hold current position for given amount of itme
    time.sleep(1.0)

    # Fix Right Foot and Free Left Foot
    motionProxy.wbFootState("Fixed", "LLeg")
    motionProxy.wbFootState("Free", "RLeg")

    # Right Ankle Dorsiflexion
    names = ["RAnklePitch"]
    angles = -0.4
    times = 1.0
    isAbsolute = True
    motionProxy.angleInterpolation(names, angles, times, isAbsolute)

    # Hold ankle position
    time.sleep(2.0)

    # Right Ankle Dorsiflexion
    names = ["RAnklePitch"]
    angles = 0.0
    times = 1.0
    isAbsolute = True
    motionProxy.angleInterpolation(names, angles, times, isAbsolute)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    motionProxy = ALProxy("ALMotion", args.ip, args.port)
    motionProxy.wakeUp()
    main(args.ip, args.port)
    motionProxy.rest()