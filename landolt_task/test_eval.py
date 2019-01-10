import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import mne
import sys
import itertools

file = sys.argv[1]
inputfile = file + '.edf'

#input file
edf = mne.io.read_raw_edf(inputfile)
stim_order = np.loadtxt("test.csv", dtype=np.int16, delimiter=',')

#create DataFrame
dataset = edf.get_data().T
Trigger_Check = dataset[:,24]

Trigger_List = []
Response_List = []
No_Response_Flag = 0
for index in range(1, len(Trigger_Check)):
	diffrence = Trigger_Check[index] - Trigger_Check[index-1]
	if diffrence == 256:
		Trigger_List.append(index)
		No_Response_Flag += 1
	elif diffrence == 8888:
		Response_List.append(index)
		No_Response_Flag = 0

	if No_Response_Flag == 2:
		Response_List.append(0)
		No_Response_Flag = 0

if len(Trigger_List) != len(Response_List):
	Response_List.append(0)

Tri_Res_array = pd.DataFrame(np.array([stim_order, Trigger_List, Response_List]).T)
Tri_Res_array.columns = ['stimulus','Trigger','Response']

#evalate and calclate Response Time
	#0,1 -> Response
	#2,3 -> None Response
HIT = MISS = FA = CR = 0
RT = [0] * len(Tri_Res_array.index)
for i,row in Tri_Res_array.iterrows():
	if row['Response'] == 0:					#None Responsed
		if row['stimulus'] == 0 or row['stimulus'] == 1:	
			MISS += 1
		else:
			CR += 1
	else:										#Responsed
		if row['stimulus'] == 0 or row['stimulus'] == 1:
			HIT += 1
		else:
			FA += 1
		RT[i] = (row['Response'] - row['Trigger']) / edf.info["sfreq"]

Tri_Res_array['RT'] = RT

result = pd.DataFrame([[HIT, MISS], [FA, CR]])
result.columns = ['Responsed', 'NonResponsed']
result.index = ['target', 'Nontarget']

#output to csv
output_array = pd.DataFrame(np.array(Tri_Res_array).T)
output_array.index = ['stimulus','Trigger','Response', 'RT']
output_array.columns = range(1, len(output_array.columns) + 1)

output_array.to_csv('{}_eval.csv'.format(file), encoding='utf-8')

result.to_csv('{}_eval.csv'.format(file), encoding='utf-8', mode='a')