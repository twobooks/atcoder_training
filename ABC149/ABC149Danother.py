N,K = map(int,input().split())
R,S,P = map(int,input().split())
T = input()

score = {"s":R, "p":S, "r":P}

ans = 0
for i in range(K):
    j = i
    tmp = ""
    while j <N:
        if tmp != T[j]:
            ans += score[T[j]]
            tmp = T[j]
        else:
            tmp = ""
        j += K

print(ans)

