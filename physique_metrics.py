import cv2
import mediapipe as mp
import numpy as np

# Set up MediaPipe Pose in static image mode
mediaPipePose = mp.solutions.pose
pose = mediaPipePose.Pose(static_image_mode=True)

# Helper function: calculate Euclidean distance between two pose landmarks
def euclideanDistance(p1, p2):
    return np.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

# Main function: extract body ratios from an input image
def extractRatios(imagePath):
    # Load and convert image to RGB (MediaPipe uses RGB)
    image = cv2.imread(imagePath)
    imageRgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Run pose detection
    results = pose.process(imageRgb)

    # Handle case where no pose is found
    if not results.pose_landmarks:
        print("❌ No pose detected.")
        return None

    # Get all 33 body landmarks
    lm = results.pose_landmarks.landmark

    # Select key landmarks for ratio calculations
    leftShoulder = lm[11]
    rightShoulder = lm[12]
    leftHip = lm[23]
    rightHip = lm[24]
    leftElbow = lm[13]
    rightElbow = lm[14]
    leftWrist = lm[15]
    rightWrist = lm[16]
    leftKnee = lm[25]
    rightKnee = lm[26]
    leftAnkle = lm[27]
    rightAnkle = lm[28]

    # Estimate height from shoulder to hip + hip to ankle
    torsoHeight = euclideanDistance(leftShoulder, leftHip)
    legLength = euclideanDistance(leftHip, leftAnkle)
    fullHeight = torsoHeight + legLength  # optional, for future use

    # Horizontal body width ratios
    shoulderWidth = euclideanDistance(leftShoulder, rightShoulder)
    waistWidth = euclideanDistance(leftHip, rightHip)

    # Arm lengths (left and right), from shoulder to wrist
    leftArmLength = euclideanDistance(leftShoulder, leftElbow) + euclideanDistance(leftElbow, leftWrist)
    rightArmLength = euclideanDistance(rightShoulder, rightElbow) + euclideanDistance(rightElbow, rightWrist)
    avgArmLength = (leftArmLength + rightArmLength) / 2

    # Leg lengths (left and right), from hip to ankle
    leftLegLength = euclideanDistance(leftHip, leftKnee) + euclideanDistance(leftKnee, leftAnkle)
    rightLegLength = euclideanDistance(rightHip, rightKnee) + euclideanDistance(rightKnee, rightAnkle)
    avgLegLength = (leftLegLength + rightLegLength) / 2

    # Return body ratios normalized by torso height
    ratios = {
        "shoulderToWaist": shoulderWidth / waistWidth if waistWidth else None,
        "armToTorso": avgArmLength / torsoHeight if torsoHeight else None,
        "legToTorso": avgLegLength / torsoHeight if torsoHeight else None,
        "upperToLowerArm": (
            (euclideanDistance(leftShoulder, leftElbow) + euclideanDistance(rightShoulder, rightElbow)) / 2
        ) / (
            (euclideanDistance(leftElbow, leftWrist) + euclideanDistance(rightElbow, rightWrist)) / 2
        ),
        "leftVsRightArm": leftArmLength / rightArmLength if rightArmLength else None
    }


    return ratios
