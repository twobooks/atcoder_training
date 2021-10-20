from numba import njit

N = int(input())

@njit
def solve(N):
    for bitlines in range(0,1<<N):
        tmp = 0
        ans = ""
        # print(bin(bitlines))
        for target in range(N-1,-1,-1):
            # print("target is ",target)
            # print("bit target is ",bin((bitlines>>target) % 2))
            if (bitlines>>target) & 1:
                tmp -= 1
                ans += ")"
            else:
                tmp += 1
                ans += "("
            if tmp>N or tmp<0:
                break
        if tmp == 0:
            print(ans)

solve(N)