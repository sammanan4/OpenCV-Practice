import cv2 as cv

img = cv.imread('DATA/00-puppy.jpg', cv.IMREAD_COLOR)

while(True):
    
    cv.imshow('Puppy', img)
    
    if cv.waitKey(1) & 0xFF == 27:
        break

cv.destroyAllWindows()