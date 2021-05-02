from heapq import heapify,heappush,heappop
import numpy as np

N = int(input())
minX = np.array(input().split(),dtype=np.int64)
maxX = minX.copy()
minX = list(minX)
maxX = list(maxX*-1)
heapify(minX)
heapify(maxX)
# print(minX,maxX)
sx = heappop(minX)
LX = heappop(maxX)*-1

while not(LX == sx):
    num = LX - sx
    # print(sx,LX,num)
    heappush(minX,num)
    heappush(maxX,num*-1)
    sx = heappop(minX)
    LX = heappop(maxX)*-1

print(sx)


