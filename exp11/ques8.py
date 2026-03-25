import pandas as pd
df_csv=pd.read_csv('C:\\Users\\student\\Desktop\\24cseaiml300\\exp11\\sample.csv')
print("Data Frame From Csv : ")
print(df_csv)

# Reading json file 
df_json=pd.read_json('C:\\Users\\student\\Desktop\\24cseaiml300\\exp11\\sample1.json')
print("\n Data Frame From Json : ")
print(df_json)