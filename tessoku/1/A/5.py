n,k=map(int,input().split())

ans=0
for x in range(1,n+1):
    for y in range(1,n+1):
        z=k-(x+y)
        if z>=1 and z<=n:
            ans+=1
print(ans)