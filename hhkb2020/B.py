H,W = map(int,input().split())
rows = []
for i in range(H):
    rows.append(input())

ans = 0
for i in range(H):
    for j in range(W):
        if j+1<W:
            if rows[i][j] == "." and  rows[i][j+1] == ".":
                ans += 1
        if i+1<H:
            if rows[i][j] == "." and  rows[i+1][j] == ".":
                ans += 1

print(ans)