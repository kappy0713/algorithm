n,m=map(int,input().split())
ab=[list(map(int,input().split())) for _ in range(m)]

g=[[] for i in range(n)] #空の2次元配列
for i in range(m):
    g[ab[i][0]-1].append(ab[i][1])
    g[ab[i][1]-1].append(ab[i][0])

for i in range(n):
    print(f"{i+1}:"+" {", end="")
    for j in range(len(g[i])):
        if j>=1:print(", ",end="")
        print(g[i][j],end="")
    print("}")