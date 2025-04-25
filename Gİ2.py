# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 16:42:32 2024

@author: edanu
"""

import cv2
import numpy as np

resim2=cv2.imread("kusResmi.jpg")


print(resim2)#her bir pikselin matrissel görünümünü verir

cv2.imshow("KUŞ RESMİ",resim2)

cv2.waitKey(0)
cv2.destroyAllWindows()


 