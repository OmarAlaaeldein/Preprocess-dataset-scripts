import os
path=os.getcwd()
for root, dirs, files in os.walk(path):
            for file in files:
                print(os.path.join(files,file))
input()