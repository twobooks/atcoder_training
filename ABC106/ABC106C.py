s = input()
k = int(input())

len1s = 0
for i in range(len(s)):
    if s[i] == "1":
        len1s += 1
        continue
    else:
        res = s[i]
        break
else:
    res = "1"

if k <= len1s:
    ans = "1"
else:
    ans = res

print(ans)
