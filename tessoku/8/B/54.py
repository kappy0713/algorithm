n = int(input())

map = {}
for i in range(n):
    a = int(input())
    if a in map:
        map[a] += 1
    else:
        map[a] = 1
ans = 0
for x in map.values():
    ans += x*(x-1)//2 # nC2(n個のものから2個取り出す)
print(ans)