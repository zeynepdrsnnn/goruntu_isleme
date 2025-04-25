# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 21:57:12 2024

@author: edanu
"""
import cv2
import numpy as numpy

resim=cv2.imread("cocuk.jpg")

kesit=resim[50:150,300:400]

resim[0:100,0:100]=kesit
#resmin kendi boyutuba dikkat etmek önemli resmin boyutunu geçmemeli 

resim[400:450,300:350]=(0,150,250)

cv2.imshow("GÖRSELDEN BİR KESİT  ALMA",resim)
cv2.imshow("GÖRSELDEN KESİT ALINDI",kesit)


cv2.waitKey(0)
cv2.destroyAllWindows()
