from collections import deque
n,x = map(int, input().split())
a = list(input())

queue = deque()
queue.append(x)
a[x-1] = "@"
while queue:
    pos = queue.popleft()
    if pos > 1:
        if a[pos - 2] == ".":
            a[pos - 2] = "@"
            queue.append(pos - 1)
    if pos < n:
        if a[pos] == ".":
            a[pos] = "@"
            queue.append(pos + 1)
print(*a,sep="")