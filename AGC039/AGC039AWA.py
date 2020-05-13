S = input()
K = int(input())

if len(S) == 1:
    print(K//2)
    exit()

if len(S)%2 == 0:
    ans = 0
    tmp = ""
    for s in S:
        if s == tmp:
            ans += 1
            tmp = ""
            continue
        else:
            tmp = s
    if S[0] == tmp:
        ans += 1
    ans *= K
    print(ans)
    exit()
else:
    len1 = len(S)-1
    S = S*2
    ans = 0
    tmp = ""
    for i in range(len(S)):
        if S[i] == tmp:
            ans += 1
            tmp = ""
            continue
        else:
            tmp = S[i]
        if i == len1:
            num = ans
    if S[0] == tmp:
        ans += 1
    d,m = divmod(K,2)
    ans = ans*d + num*m
    print(ans)
    exit()