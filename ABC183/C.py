
from itertools import permutations,combinations,combinations_with_replacement

N,K = map(int,input().split())
rows = [list(map(int,input().split())) for _ in range(N)]

routes = permutations(range(1,N))

ans = 0
for route in routes:
    tmp = rows[0][route[0]]
    for i,city in enumerate(route):
        if i+1 >= len(route):
            tmp += rows[city][0]
            break
        tmp += rows[city][route[i+1]]
    if tmp == K:
        ans += 1

print(ans)    