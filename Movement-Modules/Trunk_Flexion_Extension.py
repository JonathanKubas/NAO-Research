from naoqi import ALProxy
import argparse

def main(robotIP, PORT):
    # Initialize the proxies
    motionProxy  = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)

    # Wake up the robot
    motionProxy.wakeUp()

    # Make the robot go to sleep
    motionProxy.rest()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1", help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559, help="Robot port number")
    args = parser.parse_args()

    main(args.ip, args.port)