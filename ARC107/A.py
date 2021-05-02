A,B,C = map(int,input().split())
MOD = 998244353
ans = 1
# for a in range(1,A+1):
#     for b in range(1,B+1):
#         for c in range(1,C+1):
#             ans += a*b*c

ans *= A*(A+1)//2 % MOD
ans *= B*(B+1)//2 % MOD
ans *= C*(C+1)//2 % MOD 
print(ans%MOD)
