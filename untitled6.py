# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qPQEorgYP0m6Nw6YgMsAMW9Cz35eJyb1
"""

def tashxis (belgi):
  if belgi == "istima":
     return "Parasetamol iching"
  elif belgi == "katarakta":
     return "deksamitazon"
  elif belgi == "bosh ogʻrigʻi":
     return "trimol"
  elif belgi == "gripp":
     return "taylol hot"
  else:
     return "Shifokorga murojaat qiling"
belgi=input("Kasallik belgisini kiriting")
natija=tashxis(belgi)
print(natija)

from google.colab.patches import cv2_imshow
import cv2
def konstovar(kitob):
  if kitob == "Oʻtkan kunlar":
     rasm=cv2.imread("1447.jpg")
     cv2_imshow(rasm)
     return "29000"
  elif kitob == "Tushda kechgan umrlar":
     rasm1=cv2.imread("tkir-oshimov-tushda-kechgan-umrlar-36413-0.jpeg")
     cv2_imshow(rasm1)
     return "30000"
  elif kitob == "Daftar hoshiyasidagi bitiklar ":
     rasm2=cv2.imread("440703af02aa5c5722052ba715fee2c020220701220058751279V2vbNvOdK.jpg.webp")
     cv2_imshow(rasm2)
     return "35000"
  elif kitob == "Dunyoning ishlari ":
     rasm3=cv2.imread("Dunyoning-ishlari-muqova.jpg")
     cv2_imshow(rasm3)
     return "30000"
  elif kitob == "Sherlok Xolms ":
     rasm4=cv2.imread("2060.jpg")
     cv2_imshow(rasm4)
     return "40000"
  elif kitob == "Atom odatlar ":
     rasm5=cv2.imread("0012534847d973e1c9d270721e0f81d8202309151642268162292tjf4gum1.jpg.webp")
     cv2_imshow(rasm5)
     return "30000"
  elif kitob == "Savdogarlar ustozi ":
     rasm6=cv2.imread("qv0HZWk9P3fo5svandH90K9AyUyeQl8gsehvPT2r.jpg.webp")
     cv2_imshow(rasm6)
     return "40000"
  elif kitob == "Men":
     rasm7=cv2.imread("men.jpg")
     cv2_imshow(rasm7)
     return "45000"
  elif kitob == "Lol":
     rasm8=cv2.imread("10aa0381f4e4c21e658592b8e19c3905202309111617006813543wyazmmfe.jpg.webp")
     cv2_imshow(rasm8)
     return "40000"
  elif kitob == "Sir":
     rasm9=cv2.imread("/UuXX9ATnrwdhHNGzr7aGsENTQwZKYrbq7qmY6FLlNJIrRap41X4j527oSnOP.jpg")
     cv2_imshow(rasm9)
     return "30000"
  else:
     return "Kitob mavjud emas:"
kitob=input("Kitob nomini kiriting")
natija=konstovar(kitob)
print(natija)



