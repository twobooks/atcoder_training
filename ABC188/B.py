import numpy as np

N = input()
A = np.array(list(map(int,input().split())))
B = np.array(list(map(int,input().split())))

ans = "Yes" if np.dot(A,B)==0 else "No"
print(ans)