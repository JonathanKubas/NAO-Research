# Necessary libraries needed to 
from scipy.interpolate import interp1d
import math

# Function that calculates the left arm pitch for the robot
def leftShoulderPitch(leftArm):
    angle = 0
    if leftArm.elbowZ < leftArm.shoulderZ:
        yDistance = leftArm.shoulderY - leftArm.elbowY
        shoulderElbowDistnace = math.sqrt((leftArm.shoulderZ - leftArm.elbowZ)**2 + (leftArm.shoulderY - leftArm.elbowY)**2)
        angle = math.degrees(math.asin(yDistance / shoulderElbowDistnace))
    else: 
        shoulderYaxisDistance = leftArm.shoulderZ
        elbowYaxisDistance = math.sqrt((0 - leftArm.elbowZ)**2 + (leftArm.shoulderY - leftArm.elbowY)**2)
        shoulderElbowDistnace = math.sqrt((leftArm.shoulderZ - leftArm.elbowZ)**2 + (leftArm.shoulderY - leftArm.elbowY)**2)
        angle = math.degrees(math.acos(((shoulderElbowDistnace)**2 + (shoulderYaxisDistance)**2 - (elbowYaxisDistance)**2) / (2 * (shoulderElbowDistnace) * (shoulderYaxisDistance))))
    if angle > 119:
        angle = 119
    elif angle < 0:
        angle = 0
    angle *= (math.pi / 180)
    return angle

# Function that calculates the right arm pitch for the robot
def rightShoulderPitch(rightArm):
    angle = 0
    if rightArm.elbowZ < rightArm.shoulderZ:
        yDistance = rightArm.shoulderY - rightArm.elbowY
        shoulderElbowDistnace = math.sqrt((rightArm.shoulderZ - rightArm.elbowZ)**2 + (rightArm.shoulderY - rightArm.elbowY)**2)
        angle = math.degrees(math.asin(yDistance / shoulderElbowDistnace))
    else: 
        shoulderYaxisDistance = rightArm.shoulderZ
        elbowYaxisDistance = math.sqrt((0 - rightArm.elbowZ)**2 + (rightArm.shoulderY - rightArm.elbowY)**2)
        shoulderElbowDistnace = math.sqrt((rightArm.shoulderZ - rightArm.elbowZ)**2 + (rightArm.shoulderY - rightArm.elbowY)**2)
        angle = math.degrees(math.acos(((shoulderElbowDistnace)**2 + (shoulderYaxisDistance)**2 - (elbowYaxisDistance)**2) / (2 * (shoulderElbowDistnace) * (shoulderYaxisDistance))))
        if rightArm.elbowY > rightArm.shoulderY:
            angle *= -1
    if angle > 119:
        angle = 119
    elif angle < 0:
        angle = 0
    angle *= (math.pi / 180)
    return angle

# Function that calculates the left shoulder roll for the robot
def leftShoulderRoll(leftArm):
    xDistance = leftArm.elbowX - leftArm.shoulderX
    yDistance = leftArm.shoulderY - leftArm.elbowY
    angle = math.degrees(math.atan(xDistance / yDistance)) * -1
    if angle > 74:
        angle = 74
    elif angle < -5:
        angle = -5
    angle *= (math.pi / 180)
    return angle
    
# Function that calculates the right shoudler roll for the robot
def rightShoulderRoll(rightArm):
    xDistance = rightArm.elbowX - rightArm.shoulderX
    yDistance = rightArm.shoulderY - rightArm.elbowY
    angle = math.degrees(math.atan(xDistance / yDistance)) * -1
    if angle > 5:
        angle = 5
    elif angle < -74:
        angle = -74
    angle *= (math.pi / 180)
    return angle

# Function that calculates the left elbow roll for the robot
def leftElbowRoll(leftArm):
    a = math.sqrt((leftArm.elbowX - leftArm.shoulderX)**2 + (leftArm.elbowY - leftArm.shoulderY)**2 + (leftArm.elbowZ - leftArm.shoulderZ)**2)
    b = math.sqrt((leftArm.wristX - leftArm.elbowX)**2 + (leftArm.wristY - leftArm.elbowY)**2 + (leftArm.wristZ - leftArm.elbowZ)**2)
    c = math.sqrt((leftArm.wristX - leftArm.shoulderX)**2 + (leftArm.wristY - leftArm.shoulderY)**2 + (leftArm.wristZ - leftArm.shoulderZ)**2)
    angle = 180 - math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))
    angle *= (math.pi / 180) * (-1)
    return angle

# Function that calculates the left elbow roll for the robot
def rightElbowRoll(rightArm):
    a = math.sqrt((rightArm.elbowX - rightArm.shoulderX)**2 + (rightArm.elbowY - rightArm.shoulderY)**2 + (rightArm.elbowZ - rightArm.shoulderZ)**2)
    b = math.sqrt((rightArm.wristX - rightArm.elbowX)**2 + (rightArm.wristY - rightArm.elbowY)**2 + (rightArm.wristZ - rightArm.elbowZ)**2)
    c = math.sqrt((rightArm.wristX - rightArm.shoulderX)**2 + (rightArm.wristY - rightArm.shoulderY)**2 + (rightArm.wristZ - rightArm.shoulderZ)**2)
    angle = 180 - math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))
    angle *= (math.pi / 180)
    return angle

# Function that calculates the left hip pitch for the robot
def leftHipPitch(leftArm, leftLeg):
    yDistance = leftArm.shoulderY - leftLeg.hipY
    zDistance = leftArm.shoulderZ - leftLeg.hipZ
    angle = math.degrees(math.atan(zDistance / yDistance))
    if angle < -88:
        angle = -88
    if angle > 0:
        angle = 0
    angle *= (math.pi / 180)
    return angle

# Function that calculates the right hip pitch for the robot
def rightHipPitch(rightArm, rightLeg):
    yDistance = rightArm.shoulderY - rightLeg.hipY
    zDistance = rightArm.shoulderZ - rightLeg.hipZ
    angle = math.degrees(math.atan(zDistance / yDistance))
    if angle < -88:
        angle = -88
    if angle > 0:
        angle = 0
    angle *= (math.pi / 180)
    return angle

# Function that calculates the left hip roll for the robot
def leftHipRoll(leftLeg):
    xDistance = leftLeg.kneeX - leftLeg.hipX
    yDistance = leftLeg.hipY - leftLeg.kneeY
    angle = math.degrees(math.atan(xDistance / yDistance)) * -1
    if angle < 0:
        angle = 0
    if angle > 45:
        angle = 45
    angle *= (math.pi / 180)
    return angle

# Function that calculates the right hip roll for the robot
def rightHipRoll(rightLeg):
    xDistance = rightLeg.kneeX - rightLeg.hipX
    yDistance = rightLeg.hipY - rightLeg.kneeY
    angle = math.degrees(math.atan(xDistance / yDistance)) * -1
    if angle < -45:
        angle = -45
    if angle > 45:
        angle = 45
    angle *= (math.pi / 180)
    return angle

# Function that calculates the left knee pitch for the robot
def leftKneePitch(leftLeg):
    hipKneeDistance = math.sqrt((leftLeg.hipZ - leftLeg.kneeZ)**2 + (leftLeg.hipY - leftLeg.kneeY)**2)
    kneeAnkleDistance = math.sqrt((leftLeg.kneeZ - leftLeg.ankleZ)**2 + (leftLeg.kneeY - leftLeg.ankleY)**2)
    hipAnkleDistance = math.sqrt((leftLeg.hipZ - leftLeg.ankleZ)**2 + (leftLeg.hipY - leftLeg.ankleY)**2)
    angle = 121 - math.degrees(math.acos(((hipKneeDistance)**2 + (kneeAnkleDistance)**2 - (hipAnkleDistance)**2) / (2 * (hipKneeDistance) * (kneeAnkleDistance))))
    angle *= (math.pi / 180)
    if angle > 0.7:
        angle = 0.7
    elif angle < 0:
        angle = 0
    # Maps that calculated angle value for the knee pitch and maps it to the robots range of hip motion
    interpolatedAngle = interp1d([0, 0.7], [0, 2.120198])
    angle = float(interpolatedAngle(angle))
    return angle

# Function that calculates the right knee pitch for the robot
def rightKneePitch(rightLeg):
    hipKneeDistance = math.sqrt((rightLeg.hipZ - rightLeg.kneeZ)**2 + (rightLeg.hipY - rightLeg.kneeY)**2)
    kneeAnkleDistance = math.sqrt((rightLeg.kneeZ - rightLeg.ankleZ)**2 + (rightLeg.kneeY - rightLeg.ankleY)**2)
    hipAnkleDistance = math.sqrt((rightLeg.hipZ - rightLeg.ankleZ)**2 + (rightLeg.hipY - rightLeg.ankleY)**2)
    angle = 121 - math.degrees(math.acos(((hipKneeDistance)**2 + (kneeAnkleDistance)**2 - (hipAnkleDistance)**2) / (2 * (hipKneeDistance) * (kneeAnkleDistance))))
    angle *= (math.pi / 180)
    if angle > 0.7:
        angle = 0.7
    elif angle < 0:
        angle = 0
    # Maps that calculated angle value for the knee pitch and maps it to the robots range of hip motion
    interpolatedAngle = interp1d([0, 0.7], [0, 2.120198])
    angle = float(interpolatedAngle(angle))
    return angle