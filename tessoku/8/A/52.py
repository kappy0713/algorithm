from collections import deque
n = int(input())

queue = deque()
ans = []
for i in range(n):
    query = input().split()
    if query[0] ==  "1":
        queue.append(query[1])
    elif query[0] == "2":
        ans.append(queue[0])
    else:
        queue.popleft()
        # queueの場合popleft()横で考えるからleftを付ける

for x in ans:
    print(x)