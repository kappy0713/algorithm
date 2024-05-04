def sum_paper(x, l):
    sum = 0
    for i in range(n):
        sum += x // a[i]
    return sum

n,k = map(int, input().split())
a = list(map(int, input().split()))

left,right = 0,10**9
while left <= right:
    mid = (left + right) // 2
    check = sum_paper(mid, a)
    if check >= k:
        right = mid - 1
    elif check < k:
        left = mid + 1
print(left)