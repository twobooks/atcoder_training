# import math
# from itertools import permutations as permus
# from fractions import gcd

# import numpy as np
# import scipy as scp

times = 3
cardnums = []
for _ in range(times):
    cardnums = cardnums + list(map(int,input().split()))  # S += [input()] とも書ける

n = int(input())

times = n
bingonums = []
for _ in range(times):
    bingonums = bingonums + list(map(int,input().split()))  # S += [input()] とも書ける

for bingonum in bingonums:
    cardnums = [101 if cardnum == bingonum else cardnum for cardnum in cardnums]

def bingo_check(lis:list) -> str:
    if sum(lis[0:3])==303:
        return "Yes"
    if sum(lis[3:6])==303:
        return "Yes"
    if sum(lis[6:9])==303:
        return "Yes"
    if sum([lis[0],lis[3],lis[6]])==303:
        return "Yes"
    if sum([lis[1],lis[4],lis[7]])==303:
        return "Yes"
    if sum([lis[2],lis[5],lis[8]])==303:
        return "Yes"
    if sum([lis[0],lis[4],lis[8]])==303:
        return "Yes"
    if sum([lis[2],lis[4],lis[6]])==303:
        return "Yes"
    return "No"

ans = bingo_check(cardnums)
print(ans)