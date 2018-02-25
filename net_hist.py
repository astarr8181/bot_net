#!/usr/bin/env python
#min, max, mean, media, percentiles, box and whiskers of ASN and flows by IP address per day
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
import re
import numpy as np

Data_root = 'Data'
Data_name = 'bot_net.csv'

Path_to_Data = os.path.join(Data_root, Data_name)

df = pd.DataFrame.from_csv(Path_to_Data)
df.columns = ['Date','Local_IP', 'ASN', 'Flows']

list_dates = df.Date.unique()
print(list_dates)

