import pandas as pd
import numpy as np
import pandas_profiling as pp
from pandas_profiling import ProfileReport
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv(r'C:\Users\ramgo\OneDrive\Desktop\Learn\Analysis\OlympicsAnalysis\olympics2024.csv')
print(data.head())

#print(data.describe)

rpt=ProfileReport(data)
rpt.to_file("EDA.html")

duplicates = data[data.duplicated()]
print(duplicates)

#No duplicate countries are foundd

missing_values = data.isnull().sum()
print(missing_values)

#No missing values too

# Plot horizontal bar chart for total medals by country
plt.figure(figsize=(12, 8))
sns.barplot(y='Country', x='Total', data=data, palette='viridis')
plt.title('Total Medals by Country')
plt.xlabel('Total Medals')
plt.ylabel('Country')
plt.show()
