n = int(input())

times = n
table = []
for _ in range(times):
    a = int(input())
    temp = []
    for _ in range(a):
        x , y = map(int,input().split())
        temp.append([x-1,y])
    table.append(temp)  # S += [input()] とも書ける
    
def check(i,n):
    flg = True
    for j in range(n):
        if i>>j & 1:
            for x,y in table[j]:
                if (i>>x)%2 != y:
                    flg = False
                    # print(flg)
                    return flg
    # print(flg)
    return flg

# print(table)
ans = 0
for i in range(2**n):   #bit全探索
    if check(i,n):
        ans = max(bin(i).count("1"),ans)

print(ans)
