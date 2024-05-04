n = float(input())

left, right = 0, 100
for _ in range(100):
    x = (left + right) / 2
    if x**3 + x >= n:
        right = x
    else:
        left = x
print(x)