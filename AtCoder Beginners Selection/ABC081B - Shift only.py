_ = input()
lis = map(int,input().split())
num = 50
for i in lis:
  num = min(num,bin(i)[::-1].find("1"))
  if num ==0:
    break
print(num)