n = int(input())
s = input()

len = n//2
if s == s[:len]*2:
    ans = "Yes"
else:
    ans = "No"

print(ans)