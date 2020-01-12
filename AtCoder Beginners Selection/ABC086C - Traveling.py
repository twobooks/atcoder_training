# TLEで誤答

# input
# N
# t1 x1 y1
# t2 x2 y2
# ...
# tn xn yn
# 
# output
# 旅行プランが実行可能ならYesを、不可能ならNoを出力してください。

import numpy as np

n = int(input())

travels = np.array([0,0,0])

for i in range(n):
    travels = np.append(travels,np.array(input().split(),dtype="int64"),axis=0)

travels = travels.reshape(-1,3)

result = "Yes"
for i in range(1,n+1):
    t_x_y = travels[i] - travels[i-1]
    if t_x_y[0] < abs(t_x_y[1])+abs(t_x_y[2]):
        result = "No"
        break
    elif t_x_y[0] % 2 != (abs(t_x_y[1])+abs(t_x_y[2])) % 2:
        result = "No"
        break

print(result)

    