n,m=map(int,input().split())
ab=[list(map(int,input().split())) for _ in range(m)]

g=[[] for i in range(n)] #空の2次元配列
for i in range(m):
    g[ab[i][0]-1].append(ab[i][1])
    g[ab[i][1]-1].append(ab[i][0])

maxnum=len(g[0])
ans=1
for i in range(1,n):
    if len(g[i])>maxnum:
        ans=i+1
        maxnum=len(g[i])
print(ans)