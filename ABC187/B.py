N =int(input())
points = [list(map(int,input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(i+1,N):
        yj,yi,xj,xi = points[j][1],points[i][1],points[j][0],points[i][0]
        if -1 <= (yj-yi)/(xj-xi) <= 1:
            ans += 1

print(ans)