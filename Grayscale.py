from PIL import Image
import os
path=r"C:\Users\omara\originPNG\pneumoniapng"
for i in os.listdir(path):
    if i.endswith(".png") or i.endswith(".PNG"):
        img = Image.open(os.path.join(path,i))
        imgGray = img.convert('L')
        print(i, "Success")
        imgGray.save(os.path.join(path,i))