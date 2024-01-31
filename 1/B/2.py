x=[1,2,4,5,10,20,25,50,100]
a,b=map(int,input().split())

for i in range(a,b+1):
    if i in x:
        exit(print("Yes"))
print("No")