a,b,c = map(int,input().split())

if a==b and a==c and b==c:
    ans = "No"
elif a!=b and a!=c and b!=c:
    ans = "No"
else:
    ans = "Yes"

# Yes or No
print(ans)