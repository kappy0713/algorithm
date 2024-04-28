h,w=map(int,input().split())
x=[list(map(int,input().split())) for _ in range(h)]
q=int(input())
a,b,c,d=[0]*q,[0]*q,[0]*q,[0]*q
for i in range(q):
    a[i],b[i],c[i],d[i]=map(int,input().split())

#累積和のリスト
z=[[0 for _ in range(w+1)]for _ in range(h+1)]
#横方向の和
for i in range(1,h+1):
    for j in range(1,w+1):
        z[i][j]=z[i][j-1]+x[i-1][j-1]
#縦方向の和
for j in range(1,w+1):
    for i in range(1,h+1):
        z[i][j]=z[i-1][j]+z[i][j]
#答えを出力
for i in range(q):
    ans=z[c[i]][d[i]]+z[a[i]-1][b[i]-1]-z[c[i]][b[i]-1]-z[a[i]-1][d[i]]
    print(ans)