# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 02:03:38 2019

@author: Kundan
"""

#importing Pandas for calculation
import pandas as pd

#read excel file for Sales data and create an executable Data Frame
#File name slightly changed from 'sales data 2019 1-3' to 'salesdata2019' for proper syntaxing
#Assumption: We are using Sales data from Sheet '03' and Data location
df=pd.read_excel(r"C:\Users\Kundan\Desktop\WidgetBrain_test\salesdata2019.xlsx")

#Grouping the data column, and aggregating the sales amount by Sum
#Note: aggregation could have been done using mean, min, max etc as required
df_aggr = df.groupby(pd.Grouper(key='date', freq='15T'))['amount'].agg('sum')


#create indexing for required DataFrame
df_final = df_aggr.to_frame().reset_index()
df_final.index.names=["Transactions"]

"""
Sample o/p for 

df_final.head(4)

                            date  amount
Transactions                            
0            2019-03-01 09:30:00   46.94
1            2019-03-01 09:45:00    5.99
2            2019-03-01 10:00:00   44.13
3            2019-03-01 10:15:00   29.54
"""
