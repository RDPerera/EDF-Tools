from os import listdir
import mne
import numpy as np
from os.path import isfile, join
from os.path import isfile, join
onlyfiles = [f for f in listdir('./') if isfile(join('./', f))]

for file in onlyfiles:
    if file.endswith(".edf"):
        edf = mne.io.read_raw_edf(file)
        data= edf.get_data().T
        if 'T7' in edf.ch_names:
            data=np.delete(data, edf.ch_names.index('T7'), axis=1)
            edf.ch_names.remove('T7')
        if 'Status' in edf.ch_names:
            data=np.delete(data, edf.ch_names.index('Status'), axis=1)
            edf.ch_names.remove('Status') 
        header = ','.join(edf.ch_names)
        header+=',MARKER'
        #add marker column
        marker = np.zeros(data.shape[0])
        marker[0]=1
        data = np.c_[data,marker]
        essentialChannels=['AF3', 'F7', 'F3', 'FC5', 'P7', 'O1', 'O2', 'P8', 'T8', 'FC6', 'F4', 'F8', 'AF4']

        #check whether all channels are present in the edf file
        for i in essentialChannels:
            if i not in edf.ch_names:
                print("Channel "+i+" is missing")
                exit()
        #check length of data is equal to the 14
        if data.shape[1]!=14:
            print("Number of channels in the edf file is not equal to 14")
            exit()

        np.savetxt(file.replace(".edf", ".csv"),data, delimiter=',', header=header)

    
    