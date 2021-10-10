import cv2

image = cv2.imread('Autumn.jpg')
cv2.imshow('my image', image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)
cv2.waitKey(10000)