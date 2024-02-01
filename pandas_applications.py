'''

MISM2510 Spring 2023
Benjamin Teixeira
    
Filename:
    
Description:
    
'''
#Pandas2

import pandas as pd
df=pd.read_csv("cars.csv")
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)

###describe the data
df.describe() ##basic statistics 

df.info() ##data about missing values

###first five rows
df.head(8)
df_8=df.head(8)

##ending rows
df.tail(9)

##column names
df.columns

##particular column 
df["model"]

##multiple columns, double brackets
df[['model','year']]

##get unique values in brand column
df["brand"].unique()

##get specific rows in data
df.loc[1]

df.loc[0:4] ##getting rows with index 0 to 4

df.loc[4:9]

##filtering the data
##get all ford cars
df.loc[df["brand"]=="ford"]
ford_cars=df.loc[df["brand"]=="ford"]
df.loc[df["price"]<=5000]

#get all ford cars less than 5000 usd
df.loc[(df["brand"]=="ford") & (df["price"]<=5000)]

##sort data based on price
df.sort_values(by="price",ascending=False)

##make changes to the data
##get miles/year
df["age"]=2021-df["year"]
df["miles/year"]=df["mileage"]/df["age"]

##dropping the country column 
df=df.drop(columns="country")

##column tells you affordability of the cars
df["affordability"]="affordable"

##if price is more than 12000, then affordability is expensive
df.loc[df["price"]>12000,"affordability"]="expensive"

df[["a","b","c"]]=df["condition"].str.split(' ',expand=True)

##save this csv or excel format 
df.to_csv("cars_1.csv")
df.to_excel("cars_2.xlsx")

##aggregate statisitcs of your data
#mean prices for every brand
df.groupby("brand").median()["price"]
