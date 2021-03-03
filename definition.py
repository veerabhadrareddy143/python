

def fact(n):
     fact=1;
     for i  in range(1,n+1):
        fact=fact*i;
     return fact
r=fact(5)
print(r)