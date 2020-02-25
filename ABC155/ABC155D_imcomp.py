import numpy as np

n,k = map(int,input().split())
arrA = np.array(input().split(),dtype=np.int64)

# n<=2*10^5
# k<=2*10^9くらい
# -10^9<=a<=10^9

# listをソート
arrA.sort()
# リストの形の場合分け
if 0 <= arrA[0] <= arrA[-1]:
    ans = arrA[0] * arrA[k]
elif arrA[0] <= arrA[-1] <= 0:
    ans = arrA[-1] * arrA[-k]
else:
    if arrA[-k]
    x1 = arrA[0] * arrA[-k] # 負＊正か負＊負
    x3 = arrA[0] * arrA[k] # 負＊正か負＊負
    x2 = arrA[k] * arrA[-1] # 負＊正か負＊負
    x4 = arrA[-k] * arrA[-1] # 負＊正か負＊負
    ans = min((x1,x2,x3,x4))
# k番目に小さい値をインデックス使って求める

print(ans)