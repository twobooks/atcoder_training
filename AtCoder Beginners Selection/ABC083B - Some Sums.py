# 1以上N以下の整数のうち、10進法での各桁の和がA以上B以下であるものの総和を出力せよ。
n,a,b = map(int,input().split())

somesum = 0

for num in range(1,n+1):
    ketasum = sum(map(int,str(num)))
    if a <= ketasum <= b:
        somesum += num
print(somesum)