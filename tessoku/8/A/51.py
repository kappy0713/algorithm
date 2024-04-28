from collections import deque
n = int(input())

stack = deque()
for i in range(n):
    query = input().split()
    if query[0] == "1":
        stack.append(query[1])
    elif query[0] == "2":
        print(stack[-1])
    else:
        stack.pop()