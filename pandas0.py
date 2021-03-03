import pandas as pd
from pandas import *
import numpy as np
print(pd.__version__)
arr = [1, 2, 3, 4,5]                                #list
s1 = pd.Series(arr,index=arr)
print(s1)
n=np.random.randn(5)
s2=pd.Series(n,index=arr)
print(s2)
d={"veeera":["great","super","smile"],"anna":"dgreat","akka":"shhh"}              #dictionary
c=[0,1,2]
s3=pd.Series(d)
df=pd.DataFrame(d,index=c)
#print(df)
#print(df.head(1))                       #tail,mean,median,max,min,T(transpose)


df.to_csv('veera.csv')
f=pd.read_csv('veera.csv')
print(f)

