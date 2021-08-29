#Library Installiation
import pandas as pd 
#input dataset
data=pd.read_csv("intern/input/main.csv")
# 1.Question 
newdf=data[data['COUNTRY'].str.contains("USA")]
#Output Data
newdf.to_csv('intern/output/filteredCountry.csv')
#2.Question
df1=pd.read_csv("filteredCountry.csv")
df1.head()
df1["PRICE"]=df1['PRICE'].str.replace("$","")
df1["PRICE"]=pd.to_numeric(df1["PRICE"],errors = 'coerce')
df1.head()
df2=df1.groupby('SKU').apply(lambda df: df.nsmallest(2, 'PRICE'))
result=df2[["PRICE"]]
result.to_csv('intern/output/lowestprice.csv')
