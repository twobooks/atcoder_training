from collections import deque,Counter

N = int(input())
lisB = list(map(int,input().split()))

ans = deque()
while len(lisB) > 0:
    for i in range(len(lisB)-1,-1,-1):
        if lisB[i]-1 == i:
            ans.appendleft(lisB.pop(i))
            break
    else:
        print(-1)
        exit()

print(*ans)
