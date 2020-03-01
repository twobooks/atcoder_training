# import math
# from fractions import gcd

import numpy as np
# import scipy as scp

# 入力の受け取り
n,m = map(int,input().split())
# 列ベクトルとかの受け取り
times = m
table = []
for _ in range(times):
    table.append(list(input().split()))

statusAC = {}
answer_status = {}

for question_num , ACorWA in table:
    question_num = int(question_num)
    if question_num in statusAC:
        continue
    else:
        if ACorWA == "AC":
            statusAC[question_num] = "AC"
            if question_num in answer_status:
                answer_status[question_num] += ACorWA
            else:
                answer_status[question_num] = ACorWA
        else:
            if question_num in answer_status:
                answer_status[question_num] += ACorWA
            else:
                answer_status[question_num] = ACorWA

def penalty_count(dic):
    penalty_count = 0
    for num in dic:
        if "AC" in dic[num]:
            penalty_count  += (len(dic[num])-2)//2
        else:
            continue
    return penalty_count

# print(answer_status)
ans = len(statusAC)
penalty = penalty_count(answer_status)

print(ans,penalty)