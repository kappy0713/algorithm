n,W = map(int, input().split())
w, v = [None]*n, [None]*n
for i in range(n):
    w[i], v[i] = map(int, input().split())

dp = [[10**15 for _ in range(10**5+1)] for _ in range(n+1)]
dp[0][0] = 0
for i in range(1, n+1):
    for j in range(10**5+1):
        if j < v[i-1]:
            dp[i][j] =dp[i-1][j]
        if j >= v[i-1]:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-v[i-1]] + w[i-1])

ans = 0
for i in range(10**5+1):
    if dp[n][i] <= W:
        ans = i
print(ans)