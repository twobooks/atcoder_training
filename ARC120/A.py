N = int(input())
A = list(map(int,input().split()))

maxnum = 0
sumA = 0
addnum = 0
factor_count = 0
for num_a in A:
    maxnum = max(maxnum,num_a)
    factor_count += 1
    sumA += num_a
    addnum += sumA
    ans = addnum + maxnum*factor_count
    print(ans)
