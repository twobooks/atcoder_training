N,L = list(map(int,input().split()))
K = int(input())
A = list(map(int,input().split()))

def check(mid):
    yokans = 0
    hidari_hashi = 0
    nagasa = mid
    # tmp = 0
    for i in range(N):
        if i == N-1:
            if A[i] - hidari_hashi >= nagasa and L-A[i] >= nagasa:
                yokans += 2
            elif L-hidari_hashi >= nagasa:
                yokans += 1
            elif L-hidari_hashi < nagasa:
                continue
            else:
                continue
        else:
            if A[i] - hidari_hashi < nagasa:
                continue
            else:
                yokans += 1
                hidari_hashi = A[i]
    return (yokans >= K+1)
    # return True

ok = 0
ng = L+1
while abs(ok-ng)>1:
    mid = (ok+ng)//2
    if check(mid):
        ok = mid
    else:
        ng = mid

if ok ==0:
    print(0)
else:
    print(ok)