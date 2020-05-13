from heapq import heappush,heappop

S = input()
slist = "abcdefghijklmnopqrstuvwxyz"

if S == "zyxwvutsrqponmlkjihgfedcba":
    print(-1)
    exit()

tmp =[]
T = S
if len(S)<26:
    Sset = set(S)
    for s in slist:
        if s not in Sset:
            print(S+s)
            exit()
else:
    while len(S)>0:
        tmp.append(S[-1])
        tmp.sort()
        S = S[:-1]
        for s in tmp:
            if S + s > T:
                print(S + s)
                exit()
