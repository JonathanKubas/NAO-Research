import math

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

def leftElbowRoll(leftArm):
    a = math.sqrt((leftArm.elbowX - leftArm.shoulderX)**2 + (leftArm.elbowY - leftArm.shoulderY)**2 + (leftArm.elbowZ - leftArm.shoulderZ)**2)
    b = math.sqrt((leftArm.wristX - leftArm.elbowX)**2 + (leftArm.wristY - leftArm.elbowY)**2 + (leftArm.wristZ - leftArm.elbowZ)**2)
    c = math.sqrt((leftArm.wristX - leftArm.shoulderX)**2 + (leftArm.wristY - leftArm.shoulderY)**2 + (leftArm.wristZ - leftArm.shoulderZ)**2)
    angle = 180 - math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))
    angle *= (math.pi / 180) * (-1)
    return angle

def rightElbowRoll(rightArm):
    a = math.sqrt((rightArm.elbowX - rightArm.shoulderX)**2 + (rightArm.elbowY - rightArm.shoulderY)**2 + (rightArm.elbowZ - rightArm.shoulderZ)**2)
    b = math.sqrt((rightArm.wristX - rightArm.elbowX)**2 + (rightArm.wristY - rightArm.elbowY)**2 + (rightArm.wristZ - rightArm.elbowZ)**2)
    c = math.sqrt((rightArm.wristX - rightArm.shoulderX)**2 + (rightArm.wristY - rightArm.shoulderY)**2 + (rightArm.wristZ - rightArm.shoulderZ)**2)
    angle = 180 - math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))
    angle *= (math.pi / 180)
    return angle

# def leftHipPitch():

# def rightHipPitch():

# def leftHipRoll():

# def rightHipRoll():

# def leftKneePitch(leftLeg):

# def rightKneePitch(leftLeg):

# def leftAnklePitch():

# def rightAnklePitch():

# def leftAnkleRoll():

# def rightAnkleRoll():
