n,q = map(int, input().split())
a = list(map(int, input().split()))

sum = [0]*(n+1) # 0日目の来場者数は0人
for i in range(1, n+1):
    sum[i] = a[i-1] + sum[i-1]

ans = []
for _ in range(q):
    l,r = map(int, input().split())
    res = sum[r] - sum[l-1]
    ans.append(res)
for x in ans:
    print(x)