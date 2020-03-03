# import math
# from itertools import permutations as permus
# from fractions import gcd

# import numpy as np
# import scipy as scp

# 入力の受け取り
n = int(input())
s = input()
q = int(input())

times = q

strlis = list(s)

def qtype1(strlis,i,c):
    i = int(i)
    if i == len(strlis):
        strlis.pop()
        strlis.append(c)
    elif len(strlis) >= 2:
        strlis = strlis[:i-1] + list(c) + strlis[i:]
    else:
        strlis[i-1] = c
    # print(strlis)
    return strlis

def qtype2(i,c):
    i = int(i)
    c = int(c)
    count = len(set(strlis[i-1:c]))
    print(count)

querys = []
for _ in range(times):
    querys.append(list(input().split()))

for qtype,i,c in querys:
    if qtype == "1":
        strlis = qtype1(strlis,i,c)
    elif qtype == "2":
        qtype2(i,c)