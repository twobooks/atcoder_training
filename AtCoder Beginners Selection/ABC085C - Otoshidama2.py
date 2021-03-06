# input
# N Y
# Nは1以上の2000以下の整数
# Yは1000以上20000000以下の整数で1000の倍数
#
# output
# N枚のお札の合計金額がY円となることがありえない場合は、-1-1-1と出力せよ。
# N枚のお札の合計金額がY円となることがありうる場合は、そのようなN枚のお札の組み合わせの一例を
# 「10000円札x枚、5000円札y枚、1000円札z枚」として、x、y、zを空白で区切って出力せよ。
# 複数の可能性が考えられるときは、そのうちどれを出力してもよい。

n,dama = map(int,input().split())

x,y,z = -1,-1,-1

for z1 in range(n+1):
    for y1 in range(n+1):
        if y1+z1 <= n:
            x1 = n-(y1+z1)
            if x1*10000 + y1*5000 + z1*1000 == dama:
                x,y,z = x1,y1,z1


print("{} {} {}".format(x,y,z))