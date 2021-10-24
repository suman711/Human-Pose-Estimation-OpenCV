#Importing Libraries
import numpy as np
import cv2 as cv
import mediapipe as mp

#Accessing Mediapipe solutions
pose_Sol = mp.solutions.pose
pose = pose_Sol.Pose()
poseDraw = mp.solutions.drawing_utils

#Video Processing:

poseVid = cv.VideoCapture('Videos/VID-4.mp4') #Accessing Input Videos
#poseVid = cv.VideoCapture(0) #Accessing Web Cam for Livestream

while True:
    isTrue, frame = poseVid.read()
    resized = cv.resize(frame, (700,500))

    h, w, c = resized.shape
    blank = np.zeros([h, w, c], dtype='uint8')
    blank.fill(255)

    results = pose.process(resized)
    print(results.pose_landmarks)

    #Pose Estimation
    poseDraw.draw_landmarks(resized, results.pose_landmarks, pose_Sol.POSE_CONNECTIONS,
    poseDraw.DrawingSpec(color = (0, 69, 255)), 
    poseDraw.DrawingSpec(color = (255, 255, 0)))
    cv.imshow('Pose Estimation', resized)

    #Extracted Pose
    poseDraw.draw_landmarks(blank, results.pose_landmarks, pose_Sol.POSE_CONNECTIONS,
    poseDraw.DrawingSpec(color = (0, 0, 255)), 
    poseDraw.DrawingSpec(color = (255, 0, 0)))
    cv.imshow('Extracted Pose', blank)
    
    if cv.waitKey(1) & 0xFF == ord('d'):
        break
