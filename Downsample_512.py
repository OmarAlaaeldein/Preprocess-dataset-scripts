import os
import cv2
path=r'D:\finalconvcough'# Parent(root) directory, this script will downsample every PNG within it
def Downsample(path,new_width,new_height,format):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(format) or file.endswith(format.upper()):
                img=cv2.imread(os.path.join(root,file))
                img=cv2.resize(img,(new_width,new_height))
                cv2.imwrite(os.path.join(root,file),img)
                print('Downsampled {} to ({},{})'.format(file,new_width,new_height))
    return "Completed!!!"
Downsample(path,512,512,'png')