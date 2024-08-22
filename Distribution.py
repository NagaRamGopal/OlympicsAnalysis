import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv(r'C:\Users\ramgo\OneDrive\Desktop\Learn\Analysis\OlympicsAnalysis\olympics2024.csv')

#horizontal bar chart for total medals by country
plt.figure(figsize=(12, 8))
sns.barplot(y='Country', x='Total', data=df, palette='viridis')
plt.title('Total Medals by Country')
plt.xlabel('Total Medals')
plt.ylabel('Country')
plt.show()

#pie chart
plt.figure(figsize=(10, 10))
df.set_index('Country')['Total'].plot.pie(autopct='%1.1f%%', colors=sns.color_palette('viridis', len(df)))
plt.title('Proportion of Total Medals by Country')
plt.ylabel('')
plt.show()

