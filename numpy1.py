from numpy import *
import numpy as np
"""
arr = array([8, 3, 4, 5, 63, 5, 7, 9, 5]);
print(arr.dtype)                        #to know type of data
x = linspace(2, 10, 5)                 #to give space of 5
print(x)

y = logspace(2, 3, 4, 5)                #to know values in logspace
print(y)
a=round(2.4)
print(a)
z = arange(1, 10, 3)                    #to get 3parts b/w 1,10
print(z)
d = zeros(5)
print(d)
e = ones(3)
print(e)
"""
"""
def add(x,y):
    c=x+y;
    print(c)
add(3,5)
m1=matrix('1,2,3,2;3,4,5,6;1,4,5,6')
m2=matrix('3,4,5,6;6,3,4,3;2,7,8,9')
print('m1',m1)
print(m2)
m3=m1+m2;           #v can use +,-,%,*...
print(m3)



arr=array([2,3,5,6,7])
arr1=arr.view()             #to get diffferent addresses
arr1=arr.copy()              #not to get same changes fr arr,arr1
arr[3]=4
print(arr)
print(arr1)
print(id(arr))
print(id(arr1))
"""
x=array([
            [2,3,4,5,6,7],[3,4,6,7,5,6] ])
y=x.flatten()                   #v can use such as diognal(),min(),max()....
print(y)
z=x.reshape(4,1,3)          #to get matrix form reshape(no.of matrixes,no.of rows,no.of variables)
print(z)
""" #or
m=matrix('1,2,3,4;5,6,7,8')     #directly
print(m) 
"""
""""
u=np.array([1,2,3,4])
v=np.array([1,2,3,5])
z=np.array([1,2,3,7])
a=np.array([u,v,z])
print(a)
print(a.shape)
print(a.size)
ZA=np.zeros((3,3))
print(ZA)
print(a[0,0])
print(u.sum())
print(a.cumsum())
print(a.prod())
print(a.cumprod())
"""
