n = int(input())
s = input()

strlist = "abcdefghijklmnopqrstuvwxyz".upper()
charnum = len(strlist)

ans = ""
for i in s:
    num = strlist.index(i)
    indx = (num + n) % charnum
    anschar = strlist[indx]
    ans = ans+anschar

print(ans)
