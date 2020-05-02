N,M = map(int,input().split())

if 2*N == M:
    print(N)
    exit()
elif 2*N > M:
    print(M//2)
    exit()
else:
    rem = M-2*N
    SCCset = rem//4
    print(N+SCCset)
    exit()
