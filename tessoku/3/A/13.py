n,k = map(int, input().split())
a = list(map(int, input().split()))

# しゃくとり法
check = [0] * (n-1)

for i in range(n-1):
    if i == 0:
        check[0] = 1
    else:
        check[i] = check[i-1]
    while check[i] < n and a[check[i]] - a[i] <= k:
        check[i] += 1

ans = 0
for i in range(n-1):
    ans += check[i] - (i+1)
print(ans)