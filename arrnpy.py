from numpy import *
arr = array([8, 3, 4, 5, 63, 5, 7, 9, 5]);
print(arr.dtype)                        #to know type of data
x = linspace(2, 10, 5)                 #to give space of 5
print(x)
y = logspace(2, 3, 4, 5)                #to know values in logspace
print(y)
z = arange(1, 10, 3)                    #to get 3parts b/w 1,10
print(z)
d = zeros(5)
print(d)
e = ones(3)
print(e)
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
