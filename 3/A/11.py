n,x=map(int,input().split())
a=list(map(int,input().split()))

l,r=0,n-1
while l<=r:
    m=(l+r)//2
    if a[m]>x:
        r=m-1
    elif a[m]<x:
        l=m+1
    else:
        exit(print(m+1))