#!/usr/bin/env python
#min, max, mean, media, percentiles, box and whiskers of ASN and flows by IP address per day
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
import re
import numpy as np
import os

Data_root = 'Data'
Data_name = 'bot_net.csv'

Path_to_Data = os.path.join(Data_root, Data_name)

df = pd.DataFrame.from_csv(Path_to_Data)
df.columns = ['Date','Local_IP', 'ASN', 'Flows']

list_dates = df.Date.unique()
ips = df.Local_IP.unique()

mean_flows= df.groupby(['Date','Local_IP'], as_index=False)['Flows'].mean()
median_flows= df.groupby(['Date', 'Local_IP'], as_index=False)['Flows'].median()

df_mean = pd.DataFrame(mean_flows)
df_med = pd.DataFrame(median_flows)
df_mean_med_flows = pd.concat([mean_flows, median_flows], axis=1)
df_mean_med_flows.columns = ['Date','Local_IP', 'Flows_Mean', 'Date1','IP1', 'Flows_Median']
df_mean_med_flows.drop(['Date1', 'IP1'], axis=1)

#pd.df_mean_med.to_csv(Path_to_Data)
#print(Path_to_Data)

