from numpy import *
arr=array([2,3,5,6,7])
arr1=arr.view()             #to get diffferent addresses
arr1=arr.copy()              #not to get same changes fr arr,arr1
arr[3]=4
print(arr)
print(arr1)
print(id(arr))
print(id(arr1))
x=array([
            [2,3,4,5,6,7],[3,4,6,7,5,6] ])
y=x.flatten()                   #v can use such as diognal(),min(),max()....
print(y)
z=x.reshape(4,1,3)          #to get matrix form reshape(no.of matrixes,no.of rows,no.of variables)
print(z)
    #or
m=matrix('1,2,3,4;5,6,7,8')     #directly
print(m)
