N,M,T = map(int,input().split())

dengen = N
time = 0
for i in range(M):
    A,B = map(int,input().split())
    dengen -= A-time
    if dengen <= 0:
        print("No")
        exit()
    dengen = min(N, dengen+B-A)
    time = B

if dengen-(T-time) <= 0:
    print("No")
    exit()

print("Yes")



