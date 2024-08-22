import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv(r'C:\Users\ramgo\OneDrive\Desktop\Learn\Analysis\OlympicsAnalysis\olympics2024.csv')

df['Country'] = df['Country'].apply(lambda x: 'Others' if df[df['Country'] == x]['Total'].values[0] < 15 else x)
df_aggregated = df.groupby('Country', as_index=False)['Total'].sum()


print(df_aggregated)

plt.figure(figsize=(10, 10))
df_aggregated.set_index('Country')['Total'].plot.pie(autopct='%1.1f%%', colors=sns.color_palette('viridis', len(df)))

plt.title('Proportion of Total Medals by Country')
plt.ylabel('')
plt.show()