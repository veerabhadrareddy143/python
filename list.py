l1=[1,2,3]
l2=[3,4,5]
l3=l1+l2
print(l3)
print(l1==l2)
l4=[[5,6],[7,8],[12,45]]       #nested list
print(l4[1][1])     #printing specific element in list
l4.append('veera')
print(l4)
l4.extend(['raja'])
print(l4)
l3.remove(1)
print(l3)
l3.insert(3,15)
print(l3)
l3.pop(2)
print('pop',l3)
print(l3.count(5))              # we have sort()  ,reverse(),  copy()
lst=['big', 'small', 'medium', 'large']
lst.sort()
print(lst)
lst.reverse()
print(lst)
tup=tuple(lst)                 #converting a list into tuple
print(tup)
l5=l3[1:5:2]                    #syntax: listname[start:stop:step]
print(l5)
data=enumerate(lst)                 # this enumerate keyword is used for data handle
print(list(data))
edata=enumerate(lst,20)             #syntax:enumerate(list name,counting no. strt)
print(list(edata))