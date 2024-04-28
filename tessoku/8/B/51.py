from collections import deque

s = input()

stack = deque()
stack.append(1)
for i in range(1, len(s)):
    if s[i] == ")":
        x,y = stack.pop(),i+1 
        # stack.pop()でstackの一番上の要素を消しつつ値を代入
        print(x,y)
    else:
        stack.append(i+1)