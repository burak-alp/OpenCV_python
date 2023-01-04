import pytesseract
import numpy as np
import cv2
import imutils

img=cv2.imread('D:\\OpenCV\\test_images\\licence_plate.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
filter=cv2.bilateralFilter(gray,7,300,300)
edge=cv2.Canny(filter,30,200)

contours=cv2.findContours(edge,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnts=imutils.grab_contours(contours)
cnts=sorted(cnts,key=cv2.contourArea,reverse=True)[:10]
screen=None
for c in cnts:
    epsilon=0.002*cv2.arcLength(c,True)
    approx=cv2.approxPolyDP(c,epsilon,True)
    if len(approx) == 4:
        screen=approx
        break

mask=np.zeros(gray.shape,np.uint8)
print(screen)
new_img=cv2.drawContours(mask,[screen],0,(255,255,255),-1)
new_img=cv2.bitwise_and(img,img,mask=mask)
(x,y)=np.where(mask==255)
(topx,topy)=(np.min(x),np.min(y))
(bottomx,bottomy)=(np.max(x),np.max(y))
cropped=gray[topx:bottomx+1,topy:bottomy+1]

text=pytesseract.image_to_string((cropped,lang=="eng"))
print("detected text:",text)
cv2.imshow('edge',edge)
cv2.imshow('filter',filter)
cv2.waitKey(0)
cv2.destroyAllWindow()


