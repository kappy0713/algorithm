n = int(input())
a = list(map(int, input().split()))

q = int(input())
o,x = [0]*(n+1), [0]*(n+1)
for i in range(1, n+1):
    if a[i-1] == 1:
        o[i] = o[i-1] + 1
        x[i] = x[i-1]
    else:
        o[i] = o[i-1]
        x[i] = x[i-1] + 1

res = []
for _ in range(q):
    l,r = map(int, input().split())
    o_check = o[r] - o[l-1]
    x_check = x[r] - x[l-1]
    if o_check < x_check:
        res.append("lose")
    elif o_check > x_check:
        res.append("win")
    else:
        res.append("draw")

for s in res:
    print(s)