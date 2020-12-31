K = int(input())

check = set()

num = 0
for i in range(1,K+1):
    num = (num*10 + 7) % K
    tmp = num % K
    if tmp == 0:
        print(i)
        break
    elif tmp in check:
        print(-1)
        break
    else:
        check.add(tmp)

