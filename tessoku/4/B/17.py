n = int(input())
h = [0] + list(map(int, input().split()))

dp = [0] * (n+1)
dp[2] = abs(h[1] - h[2])
for i in range(3, n+1):
    dp[i] = min(dp[i-2] + abs(h[i-2] - h[i]), dp[i-1] + abs(h[i-1] - h[i]))

res = []
place = n
while True:
    res.append(place)
    if place <= 1:
        break
    
    if dp[place - 1] + abs(h[place - 1] - h[place]) == dp[place]:
        place -= 1
    else:
        place -= 2
print(len(res))
for x in reversed(res):
    print(x, end = " ")