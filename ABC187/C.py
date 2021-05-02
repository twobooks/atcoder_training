from collections import deque,Counter

N =int(input())
Ses = [input() for _ in range(N)]
cntS = Counter(Ses)

for s in cntS:
    if s[0]=="!":
        if s[1:] in cntS:
            print(s[1:])
            exit()
        else:
            continue
    else:
        if ("!" + s) in cntS:
            print(s)
            exit()
        else:
            continue

print("satisfiable")
        