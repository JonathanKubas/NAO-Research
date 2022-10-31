import argparse
import Sit_And_Stand
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