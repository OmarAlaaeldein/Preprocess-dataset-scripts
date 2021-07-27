import pickle as pk
import os
import shutil
directory=r"D:/Coswara-Data"
covid=pk.load(open(os.path.join(directory,"ids_covid.pkl"),'rb'))
healthy=pk.load(open(os.path.join(directory,"ids_healthy.pkl"),'rb'))
newdir=os.path.join(directory,'Extracted_data')
c=0
for i in os.listdir(newdir):
    file=os.path.join(newdir,i)
    c+=1
    if i in covid:
        try:
            os.rename(os.path.join(file,"cough-heavy.wav"),os.path.join(file,"cough-heavy{}.wav".format(c)))
            shutil.copy(os.path.join(file,"cough-heavy{}.wav".format(c)), directory+'/covidwav')

        except:
            pass
        try:
            os.rename(os.path.join(file,"cough-shallow.wav"),os.path.join(file,"cough-shallow{}.wav".format(c)))
            shutil.copy(os.path.join(file,"cough-shallow{}.wav".format(c)), directory+'/covidwav')
        except:
            pass
    elif i in healthy:
        try:
            os.rename(os.path.join(file,"cough-heavy.wav"),os.path.join(file,"cough-heavy{}.wav".format(c)))
            shutil.copy(os.path.join(file,"cough-heavy{}.wav".format(c)), directory+'/healthywav')
        except:
            pass
        try:
            os.rename(os.path.join(file,"cough-shallow.wav"),os.path.join(file,"cough-shallow{}.wav".format(c)))
            shutil.copy(os.path.join(file,"cough-shallow{}.wav".format(c)), directory+'/healthywav') 
        except:
            pass