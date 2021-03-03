import sys
sys.setrecursionlimit(20)               #setting recursion limit

print(sys.setrecursionlimit(20))

i=0

def greet():
    global i;
    i=i+1;
    print('veera is great',i)
    greet()
greet()
                            #factorial using recursion
def fact(n):
  if n==0:
      return 1
  return n*fact(n-1)
r=fact(5)
print(r)
