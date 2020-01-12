# ACになった。np.appendは遅いぽいのでlistで追加するだけ追加してからnp.arrayすれば良さそう。

import numpy as np

n = int(input())

travels = [[0,0,0]]

for i in range(n):
    travels.append(list(map(int,input().split())))

travels = np.array(travels)

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