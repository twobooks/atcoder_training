import numpy as np

H,W = map(int,input().split())
arrlist = []
for i in range(H):
    arr = np.array(list(map(int,input().split())),dtype=np.int64)
    arrlist.append(arr)

board = np.concatenate(arrlist)
minnum = np.min(board)
print(np.sum(board - minnum))