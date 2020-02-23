import math
import numpy as np

n,a,b = map(int,input().split())

def conbination(n,r):
    return math.factorial(n) / math.factorial(r) / math.factorial(n - r)

if n-a <= a:
    a = n-a
if n-b <= b:
    b = n-b

if n%2 == 0:
    arr = np.zeros(int(n/2)+1)
    arr[0] = 1
    for i in range(1,int(n/2)+1):
        arr[i] = conbination(n,i)
    answer = sum(arr)*2 - arr[a] - arr[b] -arr[int(n/2)] -1
else:
    arr = np.zeros(int(n/2)+2)
    arr[0] = 1
    for i in range(1,int(n/2)):
        arr[i] = conbination(n,i)
    answer = sum(arr)*2 - arr[a] - arr[b] -1

answer = int(answer % (10^9+7))

print(answer)