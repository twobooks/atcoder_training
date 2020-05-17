N = int(input())

if N == 1:
    print(1)
    exit()

lis = []
tmp = 0
for n in range(N+1):
    tmp += n
    lis.append(tmp)
    if tmp>=N:
        break

iranaiKazu = lis[-1] - N
for i in range(1,len(lis)):
    if i == iranaiKazu:
        continue
    print(i)