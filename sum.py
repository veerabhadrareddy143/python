
N=int(input())
A=list(map(int,input().split()))
s=[]
for i in range(N):
    s.append(A[i]+A[N-i-1])
for i in range(N):
    if(i==len(A)-1):
        print(s[i])
    else:
        print(s[i],end=' ')