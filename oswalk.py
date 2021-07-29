import os
for a,b,c  in os.walk(os.getcwd()):
    print(c)