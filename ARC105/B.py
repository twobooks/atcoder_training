# from math import gcd
import numpy as np

N = int(input())
arrA = np.array(list(map(int,input().split())))

print(np.gcd.reduce(arrA))