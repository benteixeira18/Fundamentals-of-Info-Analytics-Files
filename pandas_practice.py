'''

MISM2510 Spring 2023
Benjamin Teixeira
    
Filename: pandas1
    
Description:
    
'''
#Pandas

import pandas as pd #name as alias pd

#read file into dataframe named df
df=pd.read_excel('pokemon_data.xlsx')
#df=pd.read_csv('pokemon_data.csv') #this can be used to read a csv file

df.info() ##data about missing values

print (df.head(5)) #Reads headers and first 5 rows

print (df.columns) #Provides all the column names

print (df["Name"]) #Read a single column

print (df[["Name","Type 1"]])  #Read multiple columns

#List all unique values found in the Type 1 column
df["Type 1"].unique()

#Describe the Type 1 column data
df["Type 1"].describe()


#If you want a specific row

print (df.loc[1]) #one row, which is the 2nd row

print (df.loc[0:1]) #first two rows

print (df.loc[0:4])  #gives first five rows

print (df.loc[[0,1,5]]) #rows 1, 2, and 6


#finding specific data in the data set

print (df.loc[df['Type 1']=="Fire"]) #acts as a filter

print (df.loc[df['Type 1']=='Grass']) #more filtering

print (df.loc[df['HP']>120]) #filtering based on value

print (df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)])

df.describe() #descriptive statistics for the numerical column data


#sorting the values

print (df.sort_values(by=['Name'],ascending=True)) #this is based on single column

#Sorting values based on two columns

print (df.sort_values(by=['Type 1','HP'],ascending=True))

#if you want one ascending one descending then

ping=df.sort_values(by=['Type 1','HP'],ascending=[0,1]) #places results in new df


#Make changes to the data - add a column Total
df['Total']=df['HP']+df['Attack']+df['Defense']+df['Sp. Atk']+df['Sp. Def']+df['Speed']

#creating a list
ding=list(df['Total']) #creates list named ding

#drop a column
df=df.drop(columns=['Total'])


#change a value in first row
df.loc[0,"Name"] = 'Joker'

df.loc[[0,5],"Name"] = 'Batman' #rows 1 and 6

df.loc[0,"HP"] = 30

#Add column Age and set all to 20
df["Age"]=20

#Makes all names Orange
df["Name"]='Orange'

#Add 1 to all the HP
df["HP"]=df["HP"]+1

#Dividing a column by a number
df["HP"]=df["HP"]/2

#creating a new column that is 10 more than HP
df["HPMORE"]=df["HP"]+10


#IF HP is greater than 120, then change name to Great Scott
df.loc[df["HP"] > 120, 'Name'] = "Great Scott"

#IF HP is greater than 120, then set HP = 1000
df.loc[df["HP"] > 120, 'HP'] = 1000


#If HP is greater than 80, then do a mathematical operation
df.loc[df["HP"] > 80, 'Attack'] = df["Attack"]*100


#saving the modified df now

df.to_excel('modified.xlsx') #Excel format, leaves index columm

#df.to_csv('modified.csv',index=False) #csv format without index column
