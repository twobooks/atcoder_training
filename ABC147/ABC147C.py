n = int(input())

times = n
table = []
for _ in range(times):
    a = int(input())
    temp = []
    for _ in range(a):
        temp.append(list(map(int,input().split())))
    table.append(temp)  # S += [input()] とも書ける
    
def check(i,n):
    honestOrUnkind = [0]*n
    honestOrUnkind[i] = 1
    for item in table[i]:
        membernum = item[0]-1
        honestOrUnkind[membernum] = item[1]
    for idx,hOrU in enumerate(honestOrUnkind):
        if hOrU == 1:
            for item in table[idx]:
                membernum = item[0]-1
                if honestOrUnkind[membernum] != item[1]:
                    return False,honestOrUnkind
                else:
                    honestOrUnkind[membernum] = item[1]
                    continue
        else:
            continue    
    return True,honestOrUnkind

member = [None]*n
ans = 0
for i in range(n):
    flg , memberlist = check(i,n)
    if flg:
        # member[i] = 1
        ans = max(memberlist.count(1),ans)
    else:
        member[i] = 0

print(ans)
