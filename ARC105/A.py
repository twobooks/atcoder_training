ABCD = list(map(int,input().split()))
num = sum(ABCD)

def solve(lis,tmp,n):
    global ans
    if n > 3:
        return
    # print(tmp+lis[n],tmp)
    if tmp+lis[n] == target:
        ans = max(ans,1)
        return
    solve(ABCD,tmp+lis[n],n+1)
    solve(ABCD,tmp,n+1)

if num % 2 ==1:
    print("No")
    exit()

target = num//2
ans = 0
solve(ABCD,0,0)
print("Yes" if ans ==1 else "No")