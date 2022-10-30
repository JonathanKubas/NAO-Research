import argparse
from naoqi import ALProxy

def jointRotation(motionProxy, names, angles, times, isAbsolute):
    motionProxy.angleInterpolation(names, angles, times, isAbsolute)

def main(robotIP, PORT=9559):
    # Set prooxies for ALMotion and ALRobotPosture modules to access their methods
    motionProxy = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)
    
    # Wake up robot
    motionProxy.wakeUp()

    # Send robot to Stand Init
    postureProxy.goToPosture("StandInit", 0.5)

    # Right and Left Shoulder Pitch/Roll
    jointRotation(motionProxy, ["LShoulderPitch", "LShoulderRoll"], [0.15, -0.15], 1.0, True)
    jointRotation(motionProxy, ["RShoulderPitch", "RShoulderRoll"], [1.0, 0.15], 1.0, True)

    # Right and Left Elbow Yaw
    jointRotation(motionProxy, "LElbowYaw", 0.0, 1.0, True)
    jointRotation(motionProxy, "RElbowYaw", 0.0, 1.0, True)

    # Right and Left Elbow Roll
    jointRotation(motionProxy, "LElbowRoll", -1.5, 1.0, True)
    jointRotation(motionProxy, "RElbowRoll", 1.5, 1.0, True)

    #effector   = "LElbowRoll"
    #frame      = motion.FRAME_TORSO
    #axisMask   = almath.AXIS_MASK_VEL # just control position
    #useSensorValues = False

    #path = []
    #currentTf = motionProxy.getTransform(effector, frame, useSensorValues)
    #targetTf  = almath.Transform(currentTf)
    #targetTf.r1_c4 -= 0.04 # x
    #targetTf.r2_c4 -= 0.06 # y
    #targetTf.r3_c4 += 0.06 # z

    #path.append(list(targetTf.toVector()))
    #path.append(currentTf)

    # Go to the target and back again
    #times = [2.0, 4.0] # seconds

    #motionProxy.transformInterpolations(effector, frame, path, axisMask, times)

    # Go to rest position
    motionProxy.rest()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    main(args.ip, args.port)