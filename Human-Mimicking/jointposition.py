# Necessary imports for PyKinect2 library
from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectRuntime

# Necessary imports for NAOQI library
import argparse
from naoqi import ALProxy

# Other Imports
import time
import pygame
import ctypes
from ctypes import *
from AngleCalculations import *
import speech_recognition as sr

# Different colors for drawing skeletons 
SKELETON_COLORS = [pygame.color.THECOLORS["red"], 
                  pygame.color.THECOLORS["blue"], 
                  pygame.color.THECOLORS["green"], 
                  pygame.color.THECOLORS["orange"], 
                  pygame.color.THECOLORS["purple"], 
                  pygame.color.THECOLORS["yellow"], 
                  pygame.color.THECOLORS["violet"]]

# Class of Arm Joint Positions
class ArmJointPositions(object):
    def __init__(self, shoulderjoint, elbowjoint, wristjoint):
        self.shoulderX = shoulderjoint.Position.x
        self.shoulderY = shoulderjoint.Position.y
        self.shoulderZ = shoulderjoint.Position.z
        self.elbowX = elbowjoint.Position.x
        self.elbowY = elbowjoint.Position.y
        self.elbowZ = elbowjoint.Position.z
        self.wristX = wristjoint.Position.x
        self.wristY = wristjoint.Position.y
        self.wristZ = wristjoint.Position.z

# Class of Leg Joint Positions
class LegJointPositions(object):
    def __init__(self, hipjoint, kneejoint, anklejoint, footjoint):
        self.hipX = hipjoint.Position.x
        self.hipY = hipjoint.Position.y
        self.hipZ = hipjoint.Position.z
        self.kneeX = kneejoint.Position.x
        self.kneeY = kneejoint.Position.y
        self.kneeZ = kneejoint.Position.z
        self.ankleX = anklejoint.Position.x
        self.ankleY = anklejoint.Position.y
        self.ankleZ = anklejoint.Position.z
        self.footX = footjoint.Position.x
        self.footY = footjoint.Position.y
        self.footZ = footjoint.Position.z

# Main class of the program
class HumanMimicking(object):
    # Initialize HumanMimicking class
    def __init__(self, ip, port):
        # Set proxies for ALMotion and ALRobotPosture modules to access their methods
        self.motionProxy = ALProxy("ALMotion", ip, port)
        self.postureProxy = ALProxy("ALRobotPosture", ip, port)

        # Wake up robot and put it in standing position
        self.motionProxy.wakeUp()
        self.postureProxy.goToPosture("StandInit", 0.5)

        # Enable Whole Body Balancer and fix feet to ground
        self.motionProxy.wbEnable(True)
        self.motionProxy.wbFootState("Fixed", "Legs")

        # Initialize python game
        pygame.init()

        # Use clock to later control the frame rate of video feedback
        self._clock = pygame.time.Clock()

        # Set the height and width of python game window
        self._infoObject = pygame.display.Info()
        self._screen = pygame.display.set_mode((self._infoObject.current_w >> 1, self._infoObject.current_h >> 1), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE, 32)

        # Give python game window a title
        pygame.display.set_caption("User's Joint Positions")

        # Loop until the user clicks the close button.
        self._done = False

        # Kinect runtime object, we want only color and body frames 
        self._kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Color | PyKinectV2.FrameSourceTypes_Body | PyKinectV2.FrameSourceTypes_Depth)

        # Back buffer surface for getting Kinect color frames, 32bit color, width and height equal to the Kinect color frame size
        self._frame_surface = pygame.Surface((self._kinect.color_frame_desc.Width, self._kinect.color_frame_desc.Height), 0, 32)

        # Here we will store skeleton data 
        self._bodies = None

    # Physically draw skeletons elements on person
    def draw_body_bone(self, joints, jointPoints, color, joint0, joint1):
        joint0State = joints[joint0].TrackingState
        joint1State = joints[joint1].TrackingState

        # Both joints are not tracked
        if (joint0State == PyKinectV2.TrackingState_NotTracked) or (joint1State == PyKinectV2.TrackingState_NotTracked): 
            return

        # Both joints are not *really* tracked
        if (joint0State == PyKinectV2.TrackingState_Inferred) and (joint1State == PyKinectV2.TrackingState_Inferred):
            return

        # At least one is good 
        start = (jointPoints[joint0].x, jointPoints[joint0].y)
        end = (jointPoints[joint1].x, jointPoints[joint1].y)

        try:
            pygame.draw.line(self._frame_surface, color, start, end, 8)
        except: # need to catch it due to possible invalid positions (with inf)
            pass

    # Function to draw entire kinect skeleton
    def draw_body(self, joints, jointPoints, color):
        # Torso
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_Head, PyKinectV2.JointType_Neck)
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_Neck, PyKinectV2.JointType_SpineShoulder)
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_SpineShoulder, PyKinectV2.JointType_SpineMid)
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_SpineMid, PyKinectV2.JointType_SpineBase)
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_SpineShoulder, PyKinectV2.JointType_ShoulderRight)
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_SpineShoulder, PyKinectV2.JointType_ShoulderLeft)
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_SpineBase, PyKinectV2.JointType_HipRight)
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_SpineBase, PyKinectV2.JointType_HipLeft)
    
        # Right Arm    
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_ShoulderRight, PyKinectV2.JointType_ElbowRight)
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_ElbowRight, PyKinectV2.JointType_WristRight)
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_WristRight, PyKinectV2.JointType_HandRight)
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_HandRight, PyKinectV2.JointType_HandTipRight)
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_WristRight, PyKinectV2.JointType_ThumbRight)

        # Left Arm
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_ShoulderLeft, PyKinectV2.JointType_ElbowLeft)
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_ElbowLeft, PyKinectV2.JointType_WristLeft)
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_WristLeft, PyKinectV2.JointType_HandLeft)
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_HandLeft, PyKinectV2.JointType_HandTipLeft)
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_WristLeft, PyKinectV2.JointType_ThumbLeft)

        # Right Leg
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_HipRight, PyKinectV2.JointType_KneeRight)
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_KneeRight, PyKinectV2.JointType_AnkleRight)
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_AnkleRight, PyKinectV2.JointType_FootRight)

        # Left Leg
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_HipLeft, PyKinectV2.JointType_KneeLeft)
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_KneeLeft, PyKinectV2.JointType_AnkleLeft)
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_AnkleLeft, PyKinectV2.JointType_FootLeft)

    # Draw out the color frame
    def draw_color_frame(self, frame, target_surface):
        target_surface.lock()
        address = self._kinect.surface_as_array(target_surface.get_buffer())
        ctypes.memmove(address, frame.ctypes.data, frame.size)
        del address
        target_surface.unlock()
    # Checks the open or closed state of hands to see which feet to fix
    def hand_state_check(self, body):
      leftHandState = body.hand_left_state
      rightHandState = body.hand_right_state
      if (leftHandState not in (HandState_Open, HandState_Closed)) or (rightHandState not in (HandState_Open, HandState_Closed)):
        print("Dont change anything")
        return
      elif (leftHandState == HandState_Open) and (rightHandState == HandState_Open):
        print("Dont change anything")
        return
      elif (leftHandState == HandState_Open) and (rightHandState == HandState_Closed):
        self.motionProxy.wbFootState("Fixed", "RLeg")
        self.motionProxy.wbFootState("Free", "LLeg")
        print("Right")
        return
      elif (leftHandState == HandState_Closed) and (rightHandState == HandState_Open):
        self.motionProxy.wbFootState("Free", "RLeg")
        self.motionProxy.wbFootState("Fixed", "LLeg")
        print("Left")
        return
      elif (leftHandState == HandState_Closed) and (rightHandState == HandState_Closed):
        self.motionProxy.wbFootState("Fixed", "Legs")
        print("Both")
        return

    # Starts human mimicking process within a pygame shell
    def run(self):
        # Tells program to keep updating pygame window until user quits the game
        while not self._done:
            # Checks to see if user did something to the pygame window
            for event in pygame.event.get():
                # If yser quits the game, then the program will quit
                if event.type == pygame.QUIT:
                    self._done = True
                # Checks to see if user resized the windows
                elif event.type == pygame.VIDEORESIZE:
                    self._screen = pygame.display.set_mode(event.dict['size'], pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE, 32)

            # Get new color frame and put on pygame window
            if self._kinect.has_new_color_frame():
                frame = self._kinect.get_last_color_frame()
                self.draw_color_frame(frame, self._frame_surface)
                frame = None

            # Get new body frame
            if self._kinect.has_new_body_frame(): 
                self._bodies = self._kinect.get_last_body_frame()

            # Get new depth frame
            if self._kinect.has_new_depth_frame():
                self._depth_frame = self._kinect.get_last_depth_frame()

            # Draw skeleton, get joint data, and move nao to specific position
            if self._bodies is not None: 
                for i in range(0, self._kinect.max_body_count):
                    body = self._bodies.bodies[i]
                    if not body.is_tracked: 
                        continue 

                    joints = body.joints 
                    # Convert joint coordinates to color space 
                    joint_points = self._kinect.body_joints_to_color_space(joints)
                    self.draw_body(joints, joint_points, SKELETON_COLORS[i])

                    # Calculate and store necessary angle values
                    naoAngleValues = []
                    leftArmPositions = ArmJointPositions(joints[PyKinectV2.JointType_ShoulderLeft], joints[PyKinectV2.JointType_ElbowLeft], joints[PyKinectV2.JointType_WristLeft])
                    rightArmPosiions = ArmJointPositions(joints[PyKinectV2.JointType_ShoulderRight], joints[PyKinectV2.JointType_ElbowRight], joints[PyKinectV2.JointType_WristRight])
                    leftLegPositions = LegJointPositions(joints[PyKinectV2.JointType_HipLeft], joints[PyKinectV2.JointType_KneeLeft], joints[PyKinectV2.JointType_AnkleLeft], joints[PyKinectV2.JointType_FootLeft])
                    rightLegPositions = LegJointPositions(joints[PyKinectV2.JointType_HipRight], joints[PyKinectV2.JointType_KneeRight], joints[PyKinectV2.JointType_AnkleRight], joints[PyKinectV2.JointType_FootRight])

                    # Calculate all necessary angle values
                    naoAngleValues.append(leftShoulderPitch(leftArmPositions))
                    naoAngleValues.append(leftShoulderRoll(leftArmPositions))
                    naoAngleValues.append(leftElbowRoll(leftArmPositions))
                    naoAngleValues.append(leftHipPitch(leftArmPositions, leftLegPositions))
                    naoAngleValues.append(leftHipRoll(leftLegPositions))
                    naoAngleValues.append(leftKneePitch(leftLegPositions))
                    # naoAngleValues.append(leftAnklePitch(leftLegPositions))
                    # naoAngleValues.append(leftAnkleRoll(leftLegPositions))
                    naoAngleValues.append(rightShoulderPitch(rightArmPosiions))
                    naoAngleValues.append(rightShoulderRoll(rightArmPosiions))
                    naoAngleValues.append(rightElbowRoll(rightArmPosiions))
                    naoAngleValues.append(rightHipPitch(rightArmPosiions, rightLegPositions))
                    naoAngleValues.append(rightHipRoll(rightLegPositions))
                    naoAngleValues.append(rightKneePitch(rightLegPositions))
                    # naoAngleValues.append(rightAnklePitch(rightLegPositions))
                    print(naoAngleValues)
                    
                    # Check the hand state to see which feet to fix to floor
                    self.hand_state_check(body)                      

                    # Move nao's joints with calculated angle values
                    names = ["LShoulderPitch", "LShoulderRoll", "LElbowRoll", "LHipPitch", "LHipRoll", "LKneePitch", "RShoulderPitch", "RShoulderRoll", "RElbowRoll", "RHipPitch", "RHipRoll", "RKneePitch"]
                    angles = naoAngleValues
                    times = 0.5
                    isAbsolute = True
                    self.motionProxy.angleInterpolation(names, angles, times, isAbsolute)

            # --- copy back buffer surface pixels to the screen, resize it if needed and keep aspect ratio
            # --- (screen size may be different from Kinect's color frame size) 
            h_to_w = float(self._frame_surface.get_height()) / self._frame_surface.get_width()
            target_height = int(h_to_w * self._screen.get_width())
            surface_to_draw = pygame.transform.scale(self._frame_surface, (self._screen.get_width(), target_height))
            self._screen.blit(surface_to_draw, (0,0))
            surface_to_draw = None
            pygame.display.update()

            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # --- Limit to 60 frames per second
            self._clock.tick(4)

        # When the pygame is quitted, close the kinect and pygame window
        self._kinect.close()
        pygame.quit()

        # Send robot to rest position
        self.motionProxy.rest()

def main():
    # Create an argparse object to add command line elements. Specifically IP and Port elements.
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")
    args = parser.parse_args()

    # Create an HumanMimicking object and run the run command to start human mimicking with NAO
    game = HumanMimicking(args.ip, args.port)
    game.run()

if __name__ == "__main__":
    main()
