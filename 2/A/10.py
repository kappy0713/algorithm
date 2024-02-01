n=int(input())
a=list(map(int,input().split()))
d=int(input())
lr=[list(map(int,input().split())) for _ in range(d)]

p,q=[0]*n,[0]*n
p[0]=a[0]
q[-1]=a[-1]
for i in range(1,n):
    p[i]=max(p[i-1],a[i])
for i in reversed(range(n-1)):
    q[i]=max(q[i+1],a[i])
#答えを出力
for i in range(d):
    print(max(p[lr[i][0]-2],q[lr[i][1]]))