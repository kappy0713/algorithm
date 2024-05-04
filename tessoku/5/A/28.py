n = int(input())
ans = 0
for _ in range(n):
    ta = input().split()
    if ta[0] == "+":
        ans += int(ta[1])
    elif ta[0] == "-":
        ans -= int(ta[1])
    else:
        ans *= int(ta[1])
    ans %= 10000
    print(ans)