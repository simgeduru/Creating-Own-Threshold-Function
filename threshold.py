import cv2
import numpy as np


def threshold_own(img,thresh,maxval):
    img_copy =img.copy()
    cols,rows=img_copy.shape[:2]
    for i in range (cols):
        for j in range(rows):
            if img_copy[i,j] < thresh:
                img_copy[i,j] = 0
            else:
                img_copy[i,j] = maxval
    return thresh,img_copy