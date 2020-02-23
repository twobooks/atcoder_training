import math

n,k = map(int,input().split())

digit = int(math.log(n,k)) + 1

print(digit)