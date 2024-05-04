import math
q = int(input())
ans = []
for _ in range(q):
    x = int(input())
    flag = True
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            flag = False
            ans.append("No")
            break
    if flag:
        ans.append("Yes")
for s in ans:
    print(s)