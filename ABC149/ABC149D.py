from collections import deque,Counter

N,K = map(int,input().split())
R,S,P = map(int,input().split())
T = input()

T = T.translate(str.maketrans({'r': 'p', 's': 'r','p': 's'}))
cnt = Counter(T)
dic = {"r":R, "s":S, "p":P}

ans = cnt["r"]*R + cnt["s"]*S +cnt["p"]*P
checked = []
for i in range(N-K+1):
    if i%K in checked:
        continue
    else:
        j = i
        tmp = 0
        while j <len(T):
            if tmp == T[j]:
                ans -= dic[T[j]]
                tmp = 0
            else:
                tmp = T[j]
            j += K
        checked.append(i%K)

print(ans)

