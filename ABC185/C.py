from scipy.special import comb,perm #permはnPk

#  (N-12+11)C11
L = int(input())
ans = comb(L-1,11,True)

print(ans)

