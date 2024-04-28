n=int(input())
ans=[0]*10
for i in reversed(range(10)):
    ans[i]=n%2
    n//=2
print(*ans,sep="")