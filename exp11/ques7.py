import pandas as pd 
data={
    'Name':['Alice','Bob','charlie'],
    'Age':[25,30,35],
    'city':['New York','San Franciso','Los Angles']
}
df=pd.DataFrame(data)
print(df)
print("\n Age Column :")
print(df['Age'])
print("\n Row at index 1 :")
print(df.iloc[1])