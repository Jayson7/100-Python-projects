import cv2 
import numpy as np 

# read image 
img = cv2.imread('sam.jpg')

print(img)

# locate all edges 

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray,255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

# turn to cartoon 
color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)

cv2.imshow('Image', img)
cv2.imshow('Image', edges)
cv2.imshow('Image', cartoon)
k = cv2.imshow('Image', cartoon)

cv2.waitKey(0)
cv2.destroyAllWindows()