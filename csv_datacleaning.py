import pandas as pd
import pickle as pk
df = pd.read_csv(r'D:\Coswara-Data\combined_data.csv')
print(df.head())
df.dropna(axis=1,inplace=True)
df.dropna(axis=0,inplace=True)
print(df.head())
###### healthy
healthy = df[df['covid_status'] == 'healthy']
pk.dump(healthy['id'].tolist(),open(r'D:\Coswara-Data\ids_healthy.pkl','wb'))
########## covid
 #positive_asymp
 #positive_mild
 #positive_moderate
covid=df[df['covid_status'].isin(['positive_asymp','positive_mild','positive_moderate'])]
pk.dump(covid['id'].tolist(),open(r'D:\Coswara-Data\ids_covid.pkl','wb'))