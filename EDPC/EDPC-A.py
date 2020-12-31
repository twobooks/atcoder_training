N = int(input())
h = list(map(int,input().split()))

dp = [0]*(N+1)

dp[1] = abs(h[1]-h[0])
if N==2:
    print(dp[1])
    exit()

dp[2] = min(abs(h[2]-h[0]),dp[1]+abs(h[2]-h[1]))

for i in range(3,N):
    num1 = dp[i-1] + abs(h[i]-h[i-1])
    num2 = dp[i-2] + abs(h[i]-h[i-2])
    dp[i] = min(num1,num2)

# print(dp)
print(dp[N-1])
