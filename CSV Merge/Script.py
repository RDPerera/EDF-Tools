from os import listdir
from os.path import isfile, join
import pandas as pd
onlyfiles = [f for f in listdir('./') if isfile(join('./', f))]
data=[]
for file in onlyfiles:
    if file.endswith(".csv"):
        data.append(pd.read_csv(file, header=0))
DF=pd.concat(data)


header=['AF3', 'F7', 'F3', 'FC5', 'P7', 'O1', 'O2', 'P8', 'T8', 'FC6', 'F4', 'F8', 'AF4','MARKER']
DF.columns=header

# write data to csv with header
DF.to_csv('data.csv', index=False)

