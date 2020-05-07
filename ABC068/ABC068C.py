N,M = map(int,input().split())
rows = [list(map(int,input().split())) for _ in range(M)]

set_land1 = set()
set_landN = set()
for i in range(M):
    if rows[i][0]==1 or rows[i][1]==1:
        set_land1.add(rows[i][0])
        set_land1.add(rows[i][1])
    elif rows[i][0]==N or rows[i][1]==N:
        set_landN.add(rows[i][0])
        set_landN.add(rows[i][1])

set_root = set_land1 - set_landN
ans = "POSSIBLE"
if len(set_land1) == len(set_root):
    ans = "IMPOSSIBLE"

print(ans)
