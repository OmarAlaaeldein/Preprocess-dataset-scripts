import os
l=[]
for i in os.listdir(r"F:/Games"):
    l.append(str(i))
    print(i)
with open("files.txt",'w+') as f:
    for i in range(len(l)):
        f.writelines("{}: {}\n".format(i+1,l[i]))
