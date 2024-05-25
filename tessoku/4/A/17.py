n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [0] * n
dp[1] = a[0]
for i in range(2, n):
    dp[i] = min(dp[i-1] + a[i-1], dp[i-2] + b[i-2]) 

res = []
place = n
while True:
    res.append(place)
    if place == 1:
        break
    
    if dp[place - 2] + a[place - 2] == dp[place -1]:
        place -= 1
    else:
        place -= 2
        
print(len(res))
for x in reversed(res):
    print(x, end = " ")