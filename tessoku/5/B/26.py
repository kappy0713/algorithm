import math
n = int(input())

# エラトステネスのふるい
check = [True for _ in range(n+1)]
for i in range(2, int(math.sqrt(n)+1)):
    for j in range(i*2, n+1, i):
        check[j] = False

for i in range(2,n+1):
    if check[i] == True:
        print(i)