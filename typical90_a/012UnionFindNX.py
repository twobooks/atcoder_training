from networkx.utils import UnionFind

H,W = list(map(int,input().split()))

uf = UnionFind()
used = [[False]*(W+4) for _ in range(H+4)]

Q = int(input())
for i in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        x,y = query[1],query[2]
        used[x][y] = True
        for ri,ci in [[1,0],[-1,0],[0,1],[0,-1]]:
            r = x + ri
            c = y + ci
            if used[r][c]:
                hash1 = (x-1)*W + (y-1)
                hash2 = (r-1)*W + (c-1)
                uf.union(hash1,hash2)
        
    else:
        ra,ca,rb,cb = query[1],query[2],query[3],query[4]
        hash1 = (ra-1)*W + (ca-1)
        hash2 = (rb-1)*W + (cb-1)
        if used[ra][ca]==False or used[rb][cb]==False:
            print("No")
        elif uf[hash1] == uf[hash2]:
            print("Yes")
        else:
            print("No")