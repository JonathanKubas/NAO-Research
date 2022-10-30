import argparse
from naoqi import ALProxy

def jointRotation(motionProxy, names, angles, times, isAbsolute):
    motionProxy.angleInterpolation(names, angles, times, isAbsolute)

def main(robotIP, PORT):
    # Set prooxies for ALMotion and ALRobotPosture modules to access their methods
    motionProxy = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)

    # Set stiffness for whole body
    motionProxy.setStiffnesses("Body", 1.0)

    # Send robot to Stand Init
    postureProxy.goToPosture("StandInit", 0.5)

    # Fix both of NAO's feet to the ground
    motionProxy.wbFootState("Fixed", "Legs")

    # Right and Left Shoulder Pitch/Roll
    jointRotation(motionProxy, ["LShoulderPitch", "LShoulderRoll"], [0.15, -0.15], 1.0, True)
    jointRotation(motionProxy, ["RShoulderPitch", "RShoulderRoll"], [1.0, 0.15], 1.0, True)

    # Right and Left Elbow Yaw
    jointRotation(motionProxy, "LElbowYaw", 0.0, 1.0, True)
    jointRotation(motionProxy, "RElbowYaw", 0.0, 1.0, True)

    # Right and Left Elbow Roll
    jointRotation(motionProxy, "LElbowRoll", -1.5, 1.0, True)
    jointRotation(motionProxy, "RElbowRoll", 1.5, 1.0, True)

    # Right and Left Hip Pitch
    jointRotation(motionProxy, ["LHipPitch", "RHipPitch"], -1.0, 3.0, True)

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
