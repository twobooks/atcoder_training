s = input()

length = len(s)
acgt = set("ACGT")

ans = 0
for i in range(length):
    for j in range(length):
        moji = s[i:][::-1]
        moji = moji[j:][::-1]
        if set(moji) <= acgt:
            ans = max(ans,len(moji))

print(ans)