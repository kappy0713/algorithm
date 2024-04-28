import heapq
n = int(input())

queue = []
ans = []
# heapqだと最小値しか取得できない
# listをheapqに変換したい場合, heapq.heapify(list)
# 最大値を取得したいなら, -1倍した値を格納する
for i in range(n):
    query = input().split()
    if query[0] == "1":
        # heappushで第一引数にqueue, 第二引数に格納する値
        heapq.heappush(queue, int(query[1]))
    elif query[0] == "2":
        # heappopで最小値の取得と削除
        ans.append(heapq.heappop(queue))
        # 同時に削除されてしまうため, 取得した値を格納
        heapq.heappush(queue, ans[-1])
    else:
        heapq.heappop(queue)

for x in ans:
    print(x)