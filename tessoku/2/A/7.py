d = int(input())
n = int(input())

check = [0]*(d+2)
for i in range(n):
    l,r = map(int, input().split())
    check[l] += 1
    check[r+1] -= 1  # 出席者が減るのはr+1日目

ans = [0]*(d+1)
for i in range(1,d+1):
    ans[i] = ans[i-1] + check[i]
    print(ans[i])