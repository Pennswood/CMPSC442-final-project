import numpy as np
import pandas as pd 
import csv 
import openpyxl
import seaborn
import matplotlib.pyplot as plt

#read and store the excel  file
data_xlsx = pd.read_excel(
	'Merged.xlsx')

#write excel into csv
data_xlsx.to_csv('Merged.csv', index = None, header = True)

#convert to dataframe 
df = pd.DataFrame(pd.read_csv('Merged.csv'))

#read csv file and store
#df = pd.read_csv('Merged.csv')

#copy the file to ensure no data loss happened
df_copy = df.copy()

#change date format to str
df_copy['ActivityDate'] = df_copy['ActivityDate'].astype('str')

#fetch data using Id and Date
def get_data(Id, date):
    dt = pd.to_datetime(date) #format string to date 
    dt = dt.strftime('%Y-%m-%d') #reformat the date to remove time
    idx = df_copy[(df_copy['Id']== Id) & (df_copy['ActivityDate'] == dt)]
    #print(idx) #print specific row based on Id and date
    TotalSteps = idx.at[0, 'TotalSteps']
    TotalDistance = idx.at[0, 'TotalDistance']
    Calories = idx.at[0, 'Calories']
    TotalMinutesAsleep = idx.at[0, 'TotalMinutesAsleep']
    return (TotalSteps, TotalDistance, Calories, TotalMinutesAsleep)

def get_data_byname(name, date):
    dt = pd.to_datetime(date) #format string to date 
    dt = dt.strftime('%Y-%m-%d') #reformat the date to remove time
    idx = df_copy[(df_copy['Name']== name) & (df_copy['ActivityDate'] == dt)]
    #print(idx) #print specific row based on name and date
    TotalSteps = idx.at[0, 'TotalSteps']
    TotalDistance = idx.at[0, 'TotalDistance']
    Calories = idx.at[0, 'Calories']
    TotalMinutesAsleep = idx.at[0, 'TotalMinutesAsleep']
    return (TotalSteps, TotalDistance, Calories, TotalMinutesAsleep)

#print(df_copy.dtypes) #check datatypes

'''
def total(col):
	col = col.value_counts()
	#unique values
	idx = col.index
	#total count per unique values
	ct = col
	return(idx.values, ct.values)

p,q = total(df_copy['ActivityDate'])
print(p,q)
'''
