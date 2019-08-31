import cv2
import numpy as np

img = cv2.imread('images/circle3.png',cv2.IMREAD_UNCHANGED)
img = cv2.cvtColor(img,cv2.cv2.COLOR_RGBA2BGRA)
(h, w) = img.shape[:2]
angle90 = 90
angle180 = 180
angle270 = 270


scale = 1.0
center = (w / 2, h / 2)
n=10

for i in range(9):
    angle = 360/n
    M= cv2.getRotationMatrix2D(center,angle*(i+1),scale)
    name = "knob_" + str(i+1) + ".png"
    rotated_image=cv2.warpAffine(img,M,(w,h))
    cv2.imwrite(name,rotated_image)


cv2.destroyAllWindows()



