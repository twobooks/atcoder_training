N = int(input())
points = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    if i>=N-2:
        break
    for j in range(i+1,N):
        for k in range(j+1,N):
            dx1 = points[j][0] -points[i][0]
            dx2 = points[k][0] -points[i][0]
            dy1 = points[j][1] -points[i][1]
            dy2 = points[k][1] -points[i][1]
            if dx1*dy2 == dx2*dy1:
                print("Yes")
                exit()

print("No")


