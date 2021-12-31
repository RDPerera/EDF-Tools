from os import listdir
import mne
import numpy as np
from os.path import isfile, join
onlyfiles = [f for f in listdir('./') if isfile(join('./', f))]

for file in onlyfiles:
    if file.endswith(".edf"):
        print(file)

for file in onlyfiles:
    if file.endswith(".edf"):
        edf = mne.io.read_raw_edf(file)
        essentialChannels=['AF3', 'F7', 'F3', 'FC5', 'P7', 'O1', 'O2', 'P8', 'T8', 'FC6', 'F4', 'F8', 'AF4']
        #check whether all channels are present in the edf file
        for i in essentialChannels:
            if i not in edf.ch_names:
                print("=>>>>>>>>>>>>>>>>"+file+"Channel "+i+" is missing")
    
    