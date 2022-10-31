import argparse
import Ankle_Dorsiflexion
import Ankle_Inversion
import Sit_And_Stand
import Squat
import Thigh_Abduction
import Trunk_Flexion_Extension
from naoqi import ALProxy

def main(robotIP, PORT):
    # Enter amount of times you want to repeat the loop
    loopIterations = input("Please enter the amount of times you want this loop to run: ")

    # Set prooxies for ALMotion and ALRobotPosture modules to access their methods
    motionProxy = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)

    # Wake up robot
    motionProxy.wakeUp()

    # Send robot to standing position
    postureProxy.goToPosture("Stand", 0.5)

    # Loop through the exercises for an x amount of times
    for i in range(loopIterations):
        # Run Trunk Flexion/Extension Module
        Trunk_Flexion_Extension.main(robotIP, PORT)
        # Run Squat Module
        Squat.main(robotIP, PORT)
        # Run Thigh Abduction Module
        Thigh_Abduction.main(robotIP, PORT)
        # Run Ankle Dorsiflexion Module
        Ankle_Dorsiflexion.main(robotIP, PORT)
        # Run Ankle Inversion Module
        Ankle_Inversion.main(robotIP, PORT)
        # Run Sit And Stand Module
        Sit_And_Stand.main(robotIP, PORT)

    # Put robot to rest
    motionProxy.rest()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    main(args.ip, args.port)