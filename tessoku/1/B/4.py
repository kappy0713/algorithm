n=input()
x=len(n)
ans=0
for i in range(x):
    ans+=int(n[i])*(2**(x-1))
    x-=1
print(ans)