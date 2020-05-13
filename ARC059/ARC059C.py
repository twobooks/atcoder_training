from math import factorial,sqrt,ceil#,gcd
import numpy as np

N = int(input())
lisA = list(map(int,input().split()))
arrA = np.array(lisA)

mean = np.mean(arrA)

targetnum = round(mean)

arrans = (arrA - targetnum)**2
ans = sum(arrans)

print(int(ans))