# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 21:29:37 2024

@author: edanu
"""

import cv2
import numpy as np

sunal=cv2.imread("sunal.jpg")

#sunal[:,:,0]=255#3.parametre bgr kısmıdır ve blue kısmı devreye girer = 250 diyere blue renginin tonunu ayarlardık
#sunal[:,:,1]=255# artık green değeri için çalışır
#sunal[:,:,2]=255#red değeri için çalışır.Üçünü aynı anda kullanarak bir renk karışımı yapabilirim
#burada : yerlere değer girmediğimiz için tüm resme efekt uyguluyor.
sunal[100:200,50:100,0]=255 #şeklinde yazarak belli bi alana efekt uygular.
cv2.imshow("Efekt Uygulama",sunal)

#sadece göz kısmına bir filtre eklemek istersek



cv2.waitKey(0)
cv2.destroyAllWindows()

