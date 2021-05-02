N,X = map(int,input().split())
S = input()

for i in range(N):
    if S[i] == "o":
        X += 1
        continue
    elif S[i] == "x":
        X = max(0,X-1)
        continue
    else:
        continue

print(X)

