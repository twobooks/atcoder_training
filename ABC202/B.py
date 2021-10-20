S = input()

ans = []
for i in range(len(S)-1,-1,-1):
    tmp = int(S[i])
    if tmp==6:
        tmp += 3
    elif tmp==9:
        tmp -= 3
    ans.append(tmp)

print(*ans,sep="")