from datetime import date
import pandas as pd
import mne
import sys

file = sys.argv[1]
inputfile = file + '.edf'
outputfile = file + '_eeg.csv'

edf = mne.io.read_raw_edf(inputfile)
"""
sfreq = edf.info["sfreq"]
ex_date = date.fromtimestamp(edf.info["meas_date"][0])
highpass = edf.info["highpass"]
lowpass = edf.info["lowpass"]

ex_info = pd.Series([sfreq, ex_date, highpass, lowpass])
ex_info.index = ["sfreq","date","high","low"]

ex_info.to_csv("{}".format(outputfile), encoding='utf-8')
"""
eeg = pd.DataFrame(edf.get_data().T, columns=edf.ch_names)

#ex_infoを出力するなら mode='a' が必要
eeg.to_csv("{}".format(outputfile), encoding='utf-8', index=False)