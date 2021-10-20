from collections import Counter

L,Q = list(map(int,input().split()))

INF = L+10
dtree = {}
dtree[1] = [0,L]

def left(kireme,idx):
    if idx == 1:
        dtree[idx][0] = kireme
        return
    try:
        l,r = dtree[idx]
        if r < INF:
            dtree[idx][0] = kireme
            return
        dtree[idx][0] = kireme
        left(kireme,idx//2)
    except:
        dtree[idx] = [kireme,INF]
        left(kireme,idx//2)

def right(kireme,idx):
    if idx == 1:
        dtree[idx][1] = kireme
        return
    try:
        l,r = dtree[idx]
        if l < INF:
            dtree[idx][1] = kireme
            return
        dtree[idx][1] = kireme
        right(kireme,idx//2)
    except:
        dtree[idx] = [INF,kireme]
        right(kireme,idx//2)

def cut(kireme,idx):
    left(kireme,idx+1)
    right(kireme,idx-1)

def searchR(idx):
    if iscutted[idx]:
        return idx - leafnum
    try:
        l,r = dtree[idx]
        if r < INF:
            return r
        return searchR(idx//2)
    except:
        return searchR(idx//2)

def searchL(idx):
    if iscutted[idx]:
        return idx - leafnum
    try:
        l,r = dtree[idx]
        if l < INF:
            return l
        return searchL(idx//2)
    except:
        return searchL(idx//2)

def serchAndRes(num):
    # print(num)
    r = searchR(num+1)
    l = searchL(num-1)
    return r-l

leafnum = 1
while leafnum <= L:
    leafnum = leafnum<<1

left(0,1+leafnum)
# print(dtree)
right(L,L-1+leafnum)
# print(dtree)

iscutted = Counter()
for _ in range(Q):
    c,x = list(map(int,input().split()))
    if c==1:
        cut(x,x+leafnum)
        iscutted[x+leafnum] += 1
        # print(dtree)
    elif c==2:
        ans = serchAndRes(x+leafnum)
        print(ans)