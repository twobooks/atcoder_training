V,T,S,D = map(int,input().split())

start = V*T
end = V*S

ans = "Yes"
if start <= D <= end:
    ans = "No"

print(ans)
