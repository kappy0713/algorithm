n = int(input())
h = list(map(int, input().split()))

dp = [0] * n
dp[0] = h[0]
for i in range(1, n):
    dp[i] = min(abs(dp[i] - h[i]), abs(dp[i] - h[i-1]))
print(dp)
print(dp[-1])