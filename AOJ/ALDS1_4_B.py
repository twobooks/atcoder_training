N = int(input())
lisS = list(map(int,input().split()))
Q = int(input())
lisT = list(map(int,input().split()))


def check(mid,key):
    return lisS[mid] > key

def binary_search(key):
    OK = N #絶対Trueになるやつ
    NG = -1 #絶対Falseになるやつ
    while abs(OK-NG)>1:
        mid = (OK+NG)//2
        if check(mid,i):
            OK = mid
        else:
            NG = mid
    return lisS[NG] == key

ans = 0
for i in lisT:
    ans += binary_search(i)

print(ans)