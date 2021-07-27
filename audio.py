from scipy.io import wavfile
import os
import pickle
import keras
from keras.preprocessing import sequence
import numpy
import random
path1="D:\Project Based\coughfinaldataset1"
lol=[]
mol=[]
lol_x=[]
lol_y=[]
cat=['healthywav','covidwav']
for i in cat:
    path2=os.path.join(path1,i)
    label=cat.index(i)
    for wav in os.listdir(path2):
        wav_path=os.path.join(path2,wav)
        samplerate, data = wavfile.read(wav_path)
        if samplerate>=100000:
            continue
        lol.append([[data],label]) # enclose an array with a list in order for line 23 to work 
        mol.append(samplerate)
max_sr=max(mol)
random.shuffle(lol)
print(max_sr)
for x in lol:
    x[0] = numpy.array(sequence.pad_sequences( x[0] , maxlen=max_sr ))
for features,labels in lol:
    lol_x.append(features[0])
    lol_y.append(labels)
pickle.dump(lol_x,open('D:\wav_x.pkl','wb'))
pickle.dump(lol_y,open('D:\wav_y.pkl','wb'))
print(lol_x)