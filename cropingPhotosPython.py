# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 19:08:01 2019

@author: Shubham
"""

#convert your face into passport photos as like in studio.
from PIL import Image
catIm = Image.open('zophie.png')
catImWidth, catImHeight = catIm.size
faceIm = catIm.crop((335, 345, 565, 560))
faceImWidth, faceImHeight = faceIm.size
catCopyTwo = catIm.copy()
for left in range(0, catImWidth, faceImWidth):
    for top in range(0, catImHeight, faceImHeight):
        print(left, top)
        catCopyTwo.paste(faceIm, (left, top))
catCopyTwo.save('tiled.png')        