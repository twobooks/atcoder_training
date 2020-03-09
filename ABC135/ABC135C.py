n = int(input())
# 配列入力の受け取り
arrA = list(map(int,input().split()))
arrB = list(map(int,input().split()))

mons = arrA[n]
res = 0
for i in range(n-1,-1,-1):
    mons += arrA[i]
    if mons>=arrB[i]:
        res += arrB[i]
        mons = min(mons-arrB[i],arrA[i])
    else:
        res += mons
        mons = 0

print(res)