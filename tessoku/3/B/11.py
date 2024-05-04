n = int(input())
a = list(map(int, input().split()))

A = sorted(a)

ans = []
q = int(input())
for _ in range(q):
    x = int(input())

    left, right = 0, n-1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] >= x:
            right = mid - 1
        elif A[mid] < x:
            left = mid + 1
    ans.append(left)
for s in ans:
    print(s)