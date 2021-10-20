import math
from bisect import bisect_left

import numpy as np

N = int(input())
points = []
for i in range(N):
    X,Y = list(map(int,input().split()))
    points.append(X + Y*1.j)

ans = 0
# B点についてループ回す
for b in range(N):
    pB = points[b]
    aglDgrs = []
    # A点についてループ回す
    for a in range(N):
        if b == a:
            continue
        pA = points[a]
        # B点とA点の偏角を求めてリストにする
        aglDgrs.append(np.angle(pA - pB , deg = True))
    # C点を二分探索で求める
    aglDgrs.sort()
    ret = 0.0
    for i in range(len(aglDgrs)):
        target = aglDgrs[i] + 180
        if target >= 360:
            target -= 360
        pos1 = bisect_left(aglDgrs,target)
        if pos1 == len(aglDgrs):
            pos1 = len(aglDgrs)-1
        pos2 = 0
        if pos1 > 0:
            pos2 = pos1-1
        # print(aglDgrs,pos1,pos2)
        ang1 = abs(aglDgrs[i] - aglDgrs[pos1])
        ang2 = abs(aglDgrs[i] - aglDgrs[pos2])
        candang1 = min(ang1 , 360-ang1)
        candang2 = min(ang2 , 360-ang2)
        ret = max(ret,candang1,candang2)
    ans = max(ans , ret)

print(ans)

