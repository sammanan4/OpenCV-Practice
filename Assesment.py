import numpy as np
import cv2 as cv


def draw_circle(event, x, y, flags, param):
    
    if event == cv.EVENT_RBUTTONDOWN:
        
        cv.circle(img, (x, y), 50, (120, 240, 110), 5)


cv.namedWindow(winname = 'Puppy')

cv.setMouseCallback('Puppy', draw_circle)


img = cv.imread('DATA/dog_backpack.jpg')

while True:
    
    cv.imshow('Puppy', img)
    
    if cv.waitKey(20) & 0xFF == 27:
        
        break

cv.destroyAllWindows()