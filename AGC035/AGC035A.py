from collections import deque,Counter

N = int(input())
lisA = list(map(int,input().split()))

cnt = Counter(lisA)

if len(cnt)>3:
    print("No")
    exit()

if len(cnt) == 1:
    if lisA[0] == 0:
        print("Yes")
        exit()
    else:
        print("No")
        exit()
elif len(cnt) == 2:
    if not 0 in cnt:
        print("No")
        exit()
    else:
        keys = sorted(list(cnt.keys()))
        another = keys[-1]
        if cnt[0]*2 == cnt[another]:
            print("Yes")
            exit()
        else:
            print("No")
            exit()
else:
    keys = sorted(list(cnt.keys()))
    if keys[0]^keys[1]^keys[2] != 0:
        print("No")
        exit()
    else:
        if cnt[keys[0]]==cnt[keys[1]]==cnt[keys[2]]:
            print("Yes")
            exit()
        else:
            print("No")
            exit()
