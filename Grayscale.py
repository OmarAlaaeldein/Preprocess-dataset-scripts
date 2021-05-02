from PIL import Image
import os
path=r'C:\Users\omara\test\NORMAL'
for i in os.listdir(path):
    if i.endswith(".png"):
        img = Image.open(os.path.join(path,i))
        imgGray = img.convert('L')
        imgGray.save(os.path.join(path,i))