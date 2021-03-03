from numpy import array;
val=array('i',[3,4,5,7,8])
val.reverse()
print(val.buffer_info())
print(val)
for e in val:
    print(e)
nar=array(val.typecode,(f*f for f in val))
for i in range(5):
    print(nar[i])
