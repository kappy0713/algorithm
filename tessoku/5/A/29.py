a,b = map(int, input().split())
p,ans = a,1
for i in range(30):
    tmp = 1 << i
    if (b//tmp) % 2 == 1:
        ans = ans * p % 1000000007
    p = p * p % 1000000007
print(ans)