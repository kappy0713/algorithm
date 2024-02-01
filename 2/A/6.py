n,q=map(int,input().split())
a=list(map(int,input().split()))
lr=[list(map(int,input().split())) for _ in range(q)]

#n日目までの合計来場者を計算
ans=[0]*(n+1)
for i in range(1,n+1):
    ans[i]+=a[i-1]+ans[i-1]

for i in range(q):
    tmp=ans[lr[i][1]]-ans[lr[i][0]-1]
    print(tmp)