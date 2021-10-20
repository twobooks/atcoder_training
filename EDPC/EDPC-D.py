import numpy as np
from numba import njit

N,W = map(int,input().split())

ws = np.array([0],dtype=np.int64)
vs = np.array([0],dtype=np.int64)
for i in range(N):
    w,v = map(int,input().split())
    ws = np.append(ws,w)
    vs = np.append(vs,v)

value = np.full((N+1,W+1),-10**18,dtype=np.int64)
value[0][0] = 0

@njit
def solve(N,W,ws,vs,value):
    for i in range(1,N+1):
        for w in range(W+1):
            value[i][w] = max(value[i][w],value[i-1][w])
            if w-ws[i]>=0:
                value[i][w] = max(value[i][w],value[i-1][w-ws[i]]+vs[i])

solve(N,W,ws,vs,value)
print(np.max(value[N]))