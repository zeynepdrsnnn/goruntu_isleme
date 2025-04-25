# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 15:01:34 2024

@author: edanu
"""

import cv2
import numpy as np

resim=cv2.imread("joker.webp")

resim[50,30]=[255,255,255]#50piksel aşağıda 30 piksel sağda olan pikselin değerlerine yeni değerler atadık

for i in range(100):
    resim[70,i]=[255,255,255]

for j in range(70,100):
    resim[j,1]=[255,255,255]

cv2.imshow("Piksel Ayarlama",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()