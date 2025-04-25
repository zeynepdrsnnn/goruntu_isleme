# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 12:51:06 2024

@author: edanu
"""

import cv2
import numpy as np #burada as np ile numpy yazmadan gerekli yerde np yazdığımızda kütüphane çağırılır. np genel kullanım başka bir isimle de çağrı yapılabilir.
#as yeniden adlandırmak için bir kullanım
resim=cv2.imread("logo.png",0)#imread()resmi okumak için bir fonksiyon
#resmi okudu ve resim değişkenine atadı. burada resmi göstermez sadece resmi okur.
#burada fonksiyon içerisinde ikinci parametre olarak 0 veririsek renkleri kullanmak siyah beyaz bir görüntü oluşturur.
#Kullanım : imread("logo.png",0) şeklindedir
#cv2.den  imread fonksiyonunu aldık
#resmi görmek için imshow()fonksiyonunu kullanmak gerekir. imshow fonksiyonu da cv modülünün bir fonksiyonu olduğu için yine cv. ile kullanmak gerekir

cv2.imshow("Pencere Metni",resim)#burada göstermek istediğimiz resmi belirtmemiz gerekir. tekrar logo.png yazmaya gerek yok zaten bunu resim değişkenine atadık


cv2.imwrite("yeniresim.png",resim)#resmin orijinali var ama işelnmiş halide olsun istiyorsak bu şekilde kaydedilir.
#fonksiyonu kullanırken yeniden bir isim verilir. 2.parametrede belirrtiğimiz yeniresmi alacağımız konum


cv2.waitKey(0)#Bu kod temel iskeletin bir parçasıdır. Kapanışı yapmak için kullanılır. Pencerenin kapanması için herhangi bir tuşa basılmasını bekler.
cv2.destroyAllWindows()#Bu kod x işaretine basıldığında bağlı olan bütün pencerelerin kapanması içindir.




