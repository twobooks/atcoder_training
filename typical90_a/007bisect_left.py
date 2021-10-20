from bisect import bisect_left

NUM = (10**9)*2 + 100

N = int(input())
A = list(map(int,input().split()))
Q = int(input())

A.sort()
A = [-NUM] + A + [NUM]

# Bについて繰り返し
for i in range(Q):
    B = int(input())
    # A内をBiで二分探索
    pos = bisect_left(A,B)
    # print(pos)
    ans = min(B-A[pos-1],A[pos]-B)
    print(ans)