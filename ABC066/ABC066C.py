from collections import deque,Counter

N = int(input())
arrA = list(map(int,input().split()))

B = deque()

flg = True
for a in arrA:
    if flg:
        B.append(a)
    else:
        B.appendleft(a)
    flg = not flg
if not flg:
    B.reverse()

print(*B)