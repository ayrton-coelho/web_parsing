#!/usr/bin/python3

from PIL import Image

img = Image.open("./image/220px-Polanco_Skyline_Mexico_City_DF.jpg", "r")
pix_val = list(img.getdata())
print(pix_val)