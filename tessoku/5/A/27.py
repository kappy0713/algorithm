a,b = map(int, input().split())

# ユークリッドの互除法
# 大きい数をもう一方の数で割ったあまりに変更, これを繰り返して, 一方が0になったら終了
while a >= 1 and b >= 1:
    if b >= a:
        b %= a
    else:
        a %= b
print(max(a,b))