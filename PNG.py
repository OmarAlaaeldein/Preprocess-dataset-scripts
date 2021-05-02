from PIL import Image 
import os
directory = r'C:\Users\omara\Downloads\Hospital-Adminstration-interface-main' 
for root, dirs, files in os.walk(directory):
    for file in files: 
        if file.endswith(".jpeg"):
            file=os.path.join(root,file) 
            prefix = file.split(".jpeg")[0]
            im = Image.open(file)
            im.save(prefix+'.png')  
        else: 
            continue