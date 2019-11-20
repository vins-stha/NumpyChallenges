import pandas as pd
import numpy as np

df =pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv', usecols=[0,1,2,3,5])
#print(df.head())

df1 = df.copy()
#df1["Manufacturer","Model","Type"]=df1["Manufacturer","Model","Type"].fillna("missing")
df1.iloc[:,:3]
df1.iloc[:,:3]=df1.iloc[:,:3].fillna("missing")
df1.iloc[:,:3]=df1.iloc[:,:3].replace(np.nan, 'missing', regex=True)
df1 = df1.set_index(df1["Manufacturer"]+"_"+df1["Model"]+"_"+df1["Type"], 
                drop=True, append=False, inplace=False, verify_integrity=False)
print(df1)
