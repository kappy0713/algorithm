n,s = map(int, input().split())
a = [0] + list(map(int, input().split()))

dp = [[False for _ in range(s+1)] for _ in range(n+1)]
dp[0][0] = True

for i in range(1, n+1):
    for j in range(s+1):
        if j < a[i]:
            if dp[i-1][j] == True:
                dp[i][j] = True
            else:
                dp[i][j] = False
        
        if j >= a[i]:
            if dp[i-1][j] == True or dp[i-1][j-a[i]] == True:
                dp[i][j] = True
            else:
                dp[i][j] = False

if not dp[n][s]:
    exit(print(-1))

place = s
res = []
for i in reversed(range(1, n+1)):
    if dp[i-1][place] == True:
        pass
    else:
        place = place - a[i]
        res.append(i)

res.sort()
print(len(res))
print(*res)