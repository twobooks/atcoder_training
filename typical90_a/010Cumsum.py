N = int(input())

cumsum = [[0,0]]
for i in range(N):
    C,P = list(map(int,input().split()))
    C -= 1
    tmp = cumsum[i].copy()
    tmp[C] += P
    cumsum.append(tmp)

# print(cumsum)

Q = int(input())
for j in range(Q):
    L,R = list(map(int,input().split()))
    C1 = cumsum[R][0] - cumsum[L-1][0]
    C2 = cumsum[R][1] - cumsum[L-1][1]
    print(C1,C2)


    
