import numpy as np
import pandas as pd 
import csv 
import openpyxl
import seaborn
import matplotlib.pyplot as plt

#read and store the excel  file
# data_xlsx = pd.read_excel(
# 	'Merged.xlsx')

#write excel into csv
# data_xlsx.to_csv('Merged.csv', index = None, header = True)

#convert to dataframe 
df = pd.DataFrame(pd.read_csv('Merged.csv'))

#read csv file and store
#df = pd.read_csv('Merged.csv')

#copy the file to ensure no data loss happened
df_copy = df.copy()

#change date format to str
df_copy['ActivityDate'] = df_copy['ActivityDate'].astype('str')
#print(df_copy['ActivityDate'])

#fetch data using Id and Date
def get_data(Id, date):
    #dt = pd.to_datetime(date) #format string to date 
    #dt = dt.strftime('%Y-%m-%d') #reformat the date to remove time
    idx = df_copy[(df_copy['Id']== Id) & (df_copy['ActivityDate'] == date)]
    #print(idx) #print specific row based on Id and date
    TotalSteps = idx['TotalSteps'].iloc[0]
    TotalDistance = idx['TotalDistance'].iloc[0]
    Calories = idx['Calories'].iloc[0]
    TotalMinutesAsleep = idx['TotalMinutesAsleep'].iloc[0]
    return (TotalSteps, TotalDistance, Calories, TotalMinutesAsleep)

def get_data_byname(name, date):
    #dt = pd.to_datetime(date) #format string to date 
    #dt = dt.strftime('%Y-%m-%d') #reformat the date to remove time
    idx = df_copy[(df_copy['Name']== name) & (df_copy['ActivityDate'] == date)]
    #print(idx) #print specific row based on name and date
    TotalSteps = idx['TotalSteps'].iloc[0]
    TotalDistance = idx['TotalDistance'].iloc[0]
    Calories = idx['Calories'].iloc[0]
    TotalMinutesAsleep = idx['TotalMinutesAsleep'].iloc[0]
    return (TotalSteps, TotalDistance, Calories, TotalMinutesAsleep)

#print(df_copy.dtypes) #check datatypes

#a,b,c,d = get_data(1503960366, '29-04-2016')
#a,b,c,d = get_data_byname('Normen', '2016-04-29')
#print (a, b, c, d)


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
