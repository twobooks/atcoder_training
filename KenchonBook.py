from functools import lru_cache # 簡単メモ化 @lru_cache(maxsize=1000)

def recursiveSum(N):
    return 0 if N==0 else N + recursiveSum(N-1)

@lru_cache(maxsize=1000)
def fibo(N):
    if N==0: return 0
    elif N==1: return 1

    return fibo(N-1)+fibo(N-2)

@lru_cache(maxsize=1000)
def tribo(N):
    if N==0: return 0
    elif N==1: return 0
    elif N==2: return 1

    return tribo(N-1)+tribo(N-2)+tribo(N-3)

N = int(input())
# print(recursiveSum(N))
# print(fibo(N))
for i in range(N):
    print(tribo(i))