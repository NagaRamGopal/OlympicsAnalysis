import pandas as pd
import numpy as np
import pandas_profiling as pp
from pandas_profiling import ProfileReport
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv(r'C:\Users\ramgo\OneDrive\Desktop\Learn\Analysis\OlympicsAnalysis\olympics2024.csv')

rpt=ProfileReport(data)
rpt.to_file("EDA.html")




