from os import listdir
import mne
import numpy as np
from os.path import isfile, join
onlyfiles = [f for f in listdir('./') if isfile(join('./', f))]

print("EDF files in this directory:")
print("============================")
for file in onlyfiles:
    if file.endswith(".edf"):
        print(file)

print("\n")
print("Converting to .csv")
print("==================\n")
for file in onlyfiles:
    if file.endswith(".edf"):
        print(">>>>>>>> Converting " + file + " to .csv")
        edf = mne.io.read_raw_edf(file)
        header = ','.join(edf.ch_names)
        np.savetxt(file.replace(".edf", ".csv"), edf.get_data().T, delimiter=',', header=header)
        print("Converted " + file + " to .csv\n")
    
    