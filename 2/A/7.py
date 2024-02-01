d=int(input())
n=int(input())

#d日間の参加者数の増減を計算
attend=[0]*(d+1)
for i in range(n):
    l,r=map(int,input().split())
    attend[l-1]+=1
    attend[r]-=1

#d-1日の参加者数の増減を加算,出力
for i in range(1,d+1):
    attend[i]+=attend[i-1]
    print(attend[i-1])