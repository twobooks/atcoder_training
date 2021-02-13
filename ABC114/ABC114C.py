N = int(input())

def func(N,tmp,flg):
    global ans
    if tmp > N:
        # print(N,tmp,flg,ans)
        return
    elif flg == 0b111:
        # print(N,tmp,flg,ans)
        ans += 1
        func(N,tmp*10+3,flg | 0b001)
        func(N,tmp*10+5,flg | 0b010)
        func(N,tmp*10+7,flg | 0b100)
    else:
        func(N,tmp*10+3,flg | 0b001)
        func(N,tmp*10+5,flg | 0b010)
        func(N,tmp*10+7,flg | 0b100)

def func1(N,tmp,flg,num):
    if tmp > N:
        # print(N,tmp,flg,num)
        return
    elif flg == 0b111:
        # print(N,tmp,flg,num)
        num += 1
        func1(N,tmp*10+3,flg | 0b001,num)
        func1(N,tmp*10+5,flg | 0b010,num)
        func1(N,tmp*10+7,flg | 0b100,num)
    else:
        func1(N,tmp*10+3,flg | 0b001,num)
        func1(N,tmp*10+5,flg | 0b010,num)
        func1(N,tmp*10+7,flg | 0b100,num)
    return num

ans = 0
func(N,0,0)
# ans = func1(N,0,0,ans)
print(ans)