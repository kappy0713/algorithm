n = int(input())

map = {}
ans = []
for i in range(n):
    query = input().split()
    if query[0] == "1":
        map[query[1]] = int(query[2])
    else:
        ans.append(map[query[1]])

for x in ans:
    print(x)