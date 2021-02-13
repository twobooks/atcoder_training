import numpy as np

N = int(input())
Ai = map(int,input().split())
arrA = np.zeros(10**5+1,dtype=np.int32)
arrB = np.arange(10**5+1)
tmp = np.zeros(10**5+1,dtype=np.int32)

for a in Ai:
    tmp[a+1:] = 0
    tmp[:a+1] += 1
    arrA = np.maximum(arrA,tmp)
ans = np.max(arrA * arrB)

print(ans)
