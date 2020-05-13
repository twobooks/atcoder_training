S = input()
K = int(input())

if len(S) == 1:
    print(K//2)
    exit()

if len(set(S)) == 1:
    ans = len(S)*K//2
    print(ans)
    exit()

if S[0] != S[-1]:
    ans = 0
    tmp = ""
    for s in S:
        if s == tmp:
            ans += 1
            tmp = ""
            continue
        else:
            tmp = s
    ans *= K
    print(ans)
    exit()
elif S[0] == S[-1]:
    A = 0
    B = 0
    for s in S:
        if s == S[0]:
            A+=1
        else:
            break
    for s in S[::-1]:
        if s == S[0]:
            B+=1
        else:
            break
    ans = 0
    tmp = ""
    for s in S:
        if s == tmp:
            ans += 1
            tmp = ""
            continue
        else:
            tmp = s
    ans *= K
    ans = ans - (A//2 + B//2)*(K-1) + (A+B)//2*(K-1)
    print(ans)
    exit()
