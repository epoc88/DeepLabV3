import cv2

background = cv2.imread("back.jpg")

# Resizing image based on deeplab model 
background = cv2.resize(background, (513,384))