# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 11:18:36 2024

@author: edanu
"""
import cv2
import numpy as np

kurtResmi=cv2.imread("kurt.jpg")


cv2.imshow("PİKSEL KULLANIMI",kurtResmi)

print(kurtResmi[(230,80)])#burada yüklemiş olduğumuz resmin sol köşesi baz alınarak aşağı doğru 230 sağa doğru 80 gidilerek erişilen pikseli bulur 

print("Resmin boyutu:"+str(kurtResmi.size))#resmin boyutunu stringe çevirdik
print("Resmin Özellikleri:"+str(kurtResmi.shape))
print("Resmin Veri Tipi:"+str(kurtResmi.dtype))

cv2.waitKey(0)
cv2.destroyAllWindows()
