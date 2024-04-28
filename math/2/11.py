n = int(input())

ans = []
for i in range(2, n+1):
    flag = True
    for j in range(2, n+1):
        if i % j == 0 and i != j:
            flag = False
    if flag:
        ans.append(i)
print(*ans)