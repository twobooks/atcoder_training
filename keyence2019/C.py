from collections import deque,Counter

import numpy as np

N = int(input())
arrA = np.array(list(map(int,input().split())))
arrB = np.array(list(map(int,input().split())))

arrQ = arrA - arrB
arrQ.sort()
# num = arrQ.sum()
# if num < 0:
#     print(-1)
#     exit()

que = deque(sorted(arrQ))
tmp = 0
ans = 0
while len(que)>0:
    low = que.popleft()
    if low <0:
        tmp += low
        ans += 1
        while tmp < 0 and len(que)>0:
            tmp += que.pop()
            ans += 1
    else:
        break

if tmp < 0:
    print(-1)
    exit()

print(ans)