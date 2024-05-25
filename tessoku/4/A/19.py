n,W = map(int, input().split())
w, v = [None]*n, [None]*n
for i in range(n):
    w[i], v[i] = map(int, input().split())

dp = [[0 for _ in range(W+1)] for _ in range(n+1)]
dp[0][0] = 0
for i in range(1, n+1):
    for j in range(W+1):
        if j < w[i-1]:
            dp[i][j] =dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]] + v[i-1])

ans = 0
for i in range(W+1):
    ans = max(ans, dp[n][i])
print(ans)