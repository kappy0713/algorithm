n,k = map(int, input().split())
a = list(map(int, input().split()))

left,right = 0,n-1
count = 0
check = [0]*(n+1)
for i in range(1,n+1):
    check[i] = check[i-1] + a[i-1]

r = [0]*n
for i in range(n):
    if i == 0:
        r[i] = -1
    else:
        r[i] = r[i-1]
    while r[i] < n-1 and check[(r[i]+1)+1] - check[i] <= k:
        r[i] += 1

ans = 0
for i in range(n):
    ans += r[i] - i + 1
print(ans)