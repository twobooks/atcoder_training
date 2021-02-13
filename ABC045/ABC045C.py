S = input()
N = len(S)

ans = 0
tmp = 0
for bit in range(1 << (N-1)):
    for i in range(N):
        tmp *= 10
        tmp += int(S[i])
        if i == N-1:
            ans += tmp
            tmp = 0
            continue
        if (bit & 1<<i):
            ans += tmp
            tmp = 0
    # tmp *= 10
    # tmp += int(S[N-1])
    # ans += tmp
    # tmp = 0

print(ans)
    
