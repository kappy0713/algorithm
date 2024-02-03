import sys
sys.setrecursionlimit(10**6)

def dfs(pos):
    flag[pos]=True
    for i in g[pos]:
        if not flag[i]:dfs(i)

n,m=map(int,input().split())
ab=[list(map(int,input().split())) for _ in range(m)]

g=[[] for i in range(n+1)]
for i in range(m):
    g[ab[i][0]].append(ab[i][1])
    g[ab[i][1]].append(ab[i][0])

flag=[False]*(n+1)
dfs(1)
ans="The graph is connected."
for i in range(1,n+1):
    if flag[i]==False:
        ans="The graph is not connected."
print(ans)