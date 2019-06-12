import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
%matplotlib inline

a=[{'Year':1990,'name':'Alice','Department':'Hr','Age':25,'Salary':50000},
  {'Year':1990,'name':'Bob','Department':'Rd','Age':30,'Salary':48000},
  {'Year':1990,'name':'Charlie','Department':'Admin','Age':45,'Salary':55000},
  {'Year':1991,'name':'Alice','Department':'Hr','Age':26,'Salary':52000},
  {'Year':1991,'name':'Bob','Department':'Rd','Age':31,'Salary':50000},
  {'Year':1991,'name':'charlie','Department':'Admin','Age':46,'Salary':60000},
  {'Year':1992,'name':'Alice','Department':'ADmin','Age':27,'Salary':60000},
  {'Year':1992,'name':'Bob','Department':'Rd','Age':32,'Salary':52000},
  {'Year':1992,'name':'Charlie','Department':'Admin','Age':28,'Salary':62000}]
  a1=pd.DataFrame(a,index=[0,1,2,3,4,5,6,7,8])
print(a1)                                                                                                                                                         b=a1.groupby(['Year'])['Salary'].sum()
print("total salary spent in year",b)
c=a1.groupby(['name'])['Salary'].sum()
print("the salary recieved by each emp",c)
d=a1.groupby(['Year','Department'])['Salary'].sum()
print("salary spent on each dept",d )
