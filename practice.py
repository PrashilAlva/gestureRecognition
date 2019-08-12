import cv2

hand=cv2.imread('45Hand.jpg',0)
cv2.imshow('Original Image',hand)
ret,thresh=cv2.threshold(hand,70,225,cv2.THRESH_BINARY)
contours,hirarchy=cv2.findContours(thresh.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
hull=[cv2.convexHull(c) for c in contours]
final=cv2.drawContours(hand,hull,-1,(255,0,0))
cv2.imshow('Threshold image',thresh)
cv2.imshow('Convex Hull',final)

cv2.waitKey(0)
cv2.destroyAllWindows()