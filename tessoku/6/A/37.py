n,m,b = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))

ans = b * n * m
for x in a:
    ans += x * m

for y in c:
    ans += y * n

print(ans)