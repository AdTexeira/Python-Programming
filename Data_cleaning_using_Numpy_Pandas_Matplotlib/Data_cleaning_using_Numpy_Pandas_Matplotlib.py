# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 14:57:03 2018
Dataset taken from https://perso.telecom-paristech.fr/eagan/class/igr204/datasets
@author: Adrian Texeira
"""
#importing all the necessary libraries like numpy and pandas
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

#PANDAS AND MATPLOTLIB
#Reading input from a csv file to a dataframe
df=pd.read_csv('Camera.csv')
#returns n rows, by default returns 5 rows 
df.head()
#returns concise summary of dataframe like count of records and datatype
df.info()

#DATA CLEANING OPERATIONS
#updating column name for convinience
df.rename(columns={"Weight (inc. batteries)": "Weight"}, inplace=True)
#sorting values by Price
df.sort_values(by='Price')
#getting count of rows having weight and dimension as 0
df['Weight'][df['Weight']==0].count()
df['Dimensions'][df['Dimensions']==0].count()

#using APPLY method we can replace the values of weight by its mean, although this change does not impact the original dataframe
df['Weight'].apply(lambda x: round(df['Weight'].mean(),2) if x == 0 else round(x,2))

#In order to replace the values in original dataframe we can opt for MASK method
df['Weight'].mask(df['Weight'] == 0, round(df['Weight'].mean(),2),inplace=True)
df['Dimensions'].mask(df['Dimensions'] == 0, round(df['Dimensions'].mean(),2),inplace=True)

#checking for columns which have NULL values
null_columns=df.columns[df.isnull().any()]
null_columns
#returns count of nulls per column
df[null_columns].isnull().sum()
#calculating mean for column which has null 
df['Storage included'].mean()
#replacing NULL,NaN values with mean of respective column
df['Storage included'].fillna(df['Storage included'].mean(),inplace=True)
df['Dimensions'].fillna(df['Dimensions'].mean(),inplace=True)
df['Weight'].fillna(df['Weight'].mean(),inplace=True)
df['Macro focus range'].fillna(df['Macro focus range'].mean(),inplace=True)

#ATTRIBUTE SELECTION
#Plotting correlation matrix without Model and Release Date columns
df.drop(['Model','Release date'],axis=1).corr(method='pearson').style.format("{:.2}").background_gradient(cmap=plt.get_cmap('coolwarm'), axis=1)

#dropping Effective Pixels because it has correlation coefficient 0.94 with Max resolution, thus removing Multicollinearity in data
df.drop('Effective pixels',axis=1,inplace=True)

#DATA VISUALIZATION
#based on positive correlation coefficient plotting Price Vs Weight
df.plot(kind='scatter', x="Weight", y='Price')
plt.show()

#Plot Release date against Weight 
df.plot(kind='scatter', x="Release date", y='Weight')
plt.show()

#Plot Release date against Price 
df.plot(kind='scatter', x="Release date", y='Price')
plt.show()

#NUMPY FUNCTIONS
#converting to an array
arr_price = np.c_[df['Price']]
#finding count of prices >500
arr_price[arr_price>500].size
#converting Release date column to array
arr_years= np.c_[df['Release date']]
#Finding maximum of Release date
np.max(arr_years,axis=0)
#Finding minimun of Release date
np.min(arr_years,axis=0)
#Finding range of years using peak to peak function
np.ptp(arr_years,axis=0)