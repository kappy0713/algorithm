#2次元配列の場合,配列は大きめに取った方がよい
h,w,n=map(int,input().split())
x=[[0 for i in range(w+2)] for j in range(h+2)]
#マス目の増減
for i in range(n):
    a,b,c,d=map(int,input().split())
    x[a][b]+=1
    x[a][d+1]-=1
    x[c+1][b]-=1
    x[c+1][d+1]+=1

z=[[0 for i in range(w+2)] for j in range(h+2)]
#横方向の和
for i in range(1,h+1):
    for j in range(1,w+1):
        z[i][j]=z[i][j-1]+x[i][j]
#縦方向の和
for j in range(1,w+1):
    for i in range(1,h+1):
        z[i][j]=z[i-1][j]+z[i][j]

#答えを出力
for i in range(1,h+1):
    for j in range(1,w+1):
        print(z[i][j],end=" ")
    print(end="\n")