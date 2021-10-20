N = int(input())
graph = []
for i in range(N+1):
    graph.append([])
for i in range(2,N+1):
    graph[int(input())].append(i)

def dfs(n):
    if len(graph[n]) == 0:
        return 1
    else:
        sala = []
        for num in graph[n]:
            sala.append(dfs(num))
        return max(sala)+min(sala)+1

# print(graph)
ans = dfs(1)
print(ans)

