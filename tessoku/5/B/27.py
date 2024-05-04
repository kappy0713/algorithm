a,b = map(int, input().split())

ab = a * b
# a*b = 最小公倍数*最大公約数
while a >= 1 and b >= 1:
    if b >= a:
        b %= a
    else:
        a %= b
print(ab//max(a,b))