import pandas as pd
import numpy as np
import pandas_profiling as pp
from pandas_profiling import ProfileReport
data=pd.read_csv(r'C:\Users\ramgo\OneDrive\Desktop\Learn\Analysis\OlympicsAnalysis\olympics2024.csv')
#print(data.head())
#print(data.describe)

rpt=ProfileReport(data)
rpt.to_file("EDA.html")