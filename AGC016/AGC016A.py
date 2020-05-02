S = input()

slist = "abcdefghijklmnopqrstuvwxyz"

tmp = 0
tmps = []
ans = len(S)
for char in set(S):
    for s in S:
        if s != char:
            tmp += 1
        else:
            tmps.append(tmp)
            tmp = 0
    tmps.append(tmp)
    ans = min(ans,max(tmps))
    tmps = []
    tmp = 0

print(ans)
