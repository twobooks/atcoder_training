class UnionFind():
    "1-indexed"

    __slots__ = ["parent"]

    def __init__(self, size):
        self.parent = [-1] * (size + 1)
    
    def find(self, a):
        if self.parent[a] < 0:
            return a
        else:
            self.parent[a] = self.find(self.parent[a])
            return self.parent[a]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)

        if a == b:
            return
        else:
            if self.parent[a] == self.parent[b]:
                self.parent[a] = b
                self.parent[b] -= 1
            elif self.parent[a] < self.parent[b]: #aのほうが大きい
                self.parent[b] = a
            else:
                self.parent[a] = b #bのほうが大きい
        
    def same(self, a, b):
        return self.find(a) == self.find(b)

# class UnionFind():
#     "0-indexed"

#     __slots__ = ["parent"]

#     def __init__(self, size):
#         self.parent = [-1] * size
    
#     def find(self, a):
#         path = []
#         while self.parent[a] > 0:
#             path.append(a)
#             a = self.parent[a]
#         for child in path:
#             self.parent[child] = a
#         return a

#     def union(self, a, b):
#         a = self.find(a)
#         b = self.find(b)

#         if a == b:
#             return
#         else:
#             if self.parent[a] == self.parent[b]:
#                 self.parent[a] = b
#                 self.parent[b] -= 1
#             elif self.parent[a] < self.parent[b]: #aのほうが大きい
#                 self.parent[b] = a
#             else:
#                 self.parent[a] = b #bのほうが大きい
        
#     def same(self, a, b):
#         return self.find(a) == self.find(b)

def query1(px,py):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    for i in range(4):
        sx = px + dx[i]
        sy = py + dy[i]
        if not used[sx][sy]:
            continue
        hash1 = (px-1)*W + (py-1)
        hash2 = (sx-1)*W + (sy-1)
        uf.union(hash1,hash2)
    used[px][py] = True

def query2(px,py,qx,qy):
    if used[px][py]==False or used[qx][qy]==False:
        return False
    hash1 = (px-1)*W + (py-1)
    hash2 = (qx-1)*W + (qy-1)
    if uf.same(hash1,hash2)==True:
        return True
    return False

H,W = list(map(int,input().split()))

uf = UnionFind(H*W)
used = [[False]*(W+4) for _ in range(H+4)]

Q = int(input())
for i in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        x,y = query[1],query[2]
        query1(x,y)
    else:
        xa,ya,xb,yb = query[1],query[2],query[3],query[4]
        if query2(xa,ya,xb,yb):
            print("Yes")
        else:
            print("No")

# for i in range(H):
#     print(used[i])
# for i in range(H*W):
#     for j in range(i+1,H*W):
#         print(i,j,uf.same(i,j))