n,x = map(int, input().split())
a = list(map(int, input().split()))

left,right = 0,n-1
while left <= right:
    mid = (left + right) // 2
    if a[mid] > x:
        right = mid - 1
    elif a[mid] <x:
        left = mid + 1
    else:
        exit(print(mid + 1))