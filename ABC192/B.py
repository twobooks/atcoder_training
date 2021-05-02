S = input()

S1 = S[0::2]
S2 = S[1::2]

if S1.islower() and (S2.isupper() or not(len(S2)>1)):
    print("Yes")
else:
    print("No")