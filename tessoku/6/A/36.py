n,k = map(int, input().split())

if k >= 2 * n - 2:
    if k % 2 == 0:
        exit(print("Yes"))
print("No")