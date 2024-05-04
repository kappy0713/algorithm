n = int(input())

a = [0]*n
a[0],a[1] = 1,1
for i in range(2, n):
    a[i] = a[i-1] + a[i-2]
    a[i] %=  1000000007
print(a[-1])