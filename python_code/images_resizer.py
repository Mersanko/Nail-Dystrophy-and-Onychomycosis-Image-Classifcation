#!/usr/bin/python
from PIL import Image
import os, sys

path = "C:\\Users\\Admin\\OneDrive - g.msuiit.edu.ph\\Desktop\\pythonprojectofmylife\\datasets (B1, B2, C, D, E)\\B1\\naildystrophy\\"
# path = 'C:\\Users\\Admin\\OneDrive - g.msuiit.edu.ph\\Desktop\\pythonprojectofmylife\\datasets (B1, B2, C, D, E)\\B1\\onychomycosis\\'

dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((200, 200), Image.Resampling.LANCZOS)
            imResize.save(f + ' resized.jpg', 'JPEG', quality=100)

resize()
print('Done')
