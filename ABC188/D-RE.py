import numpy as np

N,C = map(int,input().split())

sum_arr = np.zeros(10**9,dtype=np.int32)
c_arr = np.full(10**9,C,dtype=np.int32)

for i in range(N):
    ai,bi,ci = map(int,input().split())
    sum_arr[ai-1:bi] += ci

tmp = np.minimum(sum_arr,c_arr)
ans = np.sum(tmp)
print(ans)
