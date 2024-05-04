t = int(input())
n = int(input())

check = [0]*(t+2)
for i in range(n):
    l,r = map(int, input().split())
    check[l] += 1
    check[r] -= 1

ans = [check[0]] + [0]*(t-1)
for i in range(1, t):
    ans[i] = ans[i-1] + check[i]

for i in range(t):
    print(ans[i])