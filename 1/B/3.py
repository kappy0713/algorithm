n=int(input())
a=list(map(int,input().split()))

#問題の制約条件には十分間に合うため,全探索(N<=100)
for i in range(n):
    for j in range(n):
        for k in range(n):
            if a[i]+a[j]+a[k]==1000 and (i!=j and j!=k and k!=i):
                exit(print("Yes"))
print("No") 