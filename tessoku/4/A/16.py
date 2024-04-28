# 動的計画法
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [0] * n
dp[1] = a[0]
for i in range(2, n):
    dp[i] = min(dp[i-1] + a[i-1], dp[i-2] + b[i-2]) 
print(dp[-1])