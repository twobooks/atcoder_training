import numba

# N = int(input())

# def calc(s,e):
#     end = e//s * s
#     res = (s + end)*(e//s) // 2
#     return res

# ans = 0
# for i in range(1,N+1):
#     tmp = calc(i,N)
#     ans += tmp

@numba.njit("i8(i8)")
def main(N):
    ans = 0
    for i in range(1,N+1):
        end = N//i * i
        cnt = N//i
        tmp = (i+end)*cnt // 2
        ans += tmp
    return ans

# @numba.jit
# def main(N):
#     x = 0
#     for a in range(1, N+1):
#         for b in range(1, N//a + 1):
#             x += a*b
#     return x
 
N = int(input())
print(main(N))
