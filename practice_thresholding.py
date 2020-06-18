import cv2
import numpy as np

img = cv2.imread('img/SAM_8296.jpg')
img_grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

retval, threshold = cv2.threshold(img, 60, 255, cv2.THRESH_BINARY)
retval_gray, threshold_gray = cv2.threshold(img_grayscale, 60, 255, cv2.THRESH_BINARY)

gaus = cv2.adaptiveThreshold(img_grayscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

cv2.imshow('original', img)
cv2.imshow('threshold', threshold)
cv2.imshow('threshold_gray', threshold_gray)
cv2.imshow('gaussian', gaus)

cv2.waitKey(0)
cv2.destroyAllWindows()