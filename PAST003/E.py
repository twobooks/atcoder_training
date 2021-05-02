N,M,Q = map(int,input().split())

graph = []
for i in range(0,N):
    row = []
    for j in range(0,N):
        row.append(False)
    graph.append(row)

for i in range(0,M):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    graph[u][v] = True
    graph[v][u] = True

C = list(map(int,input().split()))

querys = []
for i in range(0,Q):
    query = list(map(int,input().split()))
    querys.append(query)

for query in querys:
    if query[0] == 1:
        x = query[1]
        x -= 1
        print(C[x])
        for i in range(0,N):
            if graph[x][i] is True:
                C[i] = C[x]

    if query[0] == 2:
        x = query[1]
        y = query[2]
        x -= 1
        print(C[x])
        C[x] = y