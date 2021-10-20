from collections import deque,Counter

N,K = list(map(int,input().split()))
friendsAB = Counter()
for i in range(N):
    A,B = list(map(int,input().split()))
    friendsAB[A] += B

muraNum = 0
for mura in sorted(friendsAB):
    if K >= mura-muraNum:
        K -= mura-muraNum
        muraNum += mura-muraNum
        K += friendsAB[mura]
    else:
        muraNum += K
        K = 0
    
muraNum += K
print(muraNum)

