import math

x,y = map(int,input().split())

num = y//x
# ans = int(math.log2(num) + 1)
ans = len(bin(num))-bin(num).find('1')
print(ans)