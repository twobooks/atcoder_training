# input
# N
# d1,d2 ... dn
# 
# output
# 作ることのできる鏡餅の最大の段数を出力せよ。

n = int(input())
diameters = set()
for i in range(n):
    diameters.add(input())

print(len(diameters))