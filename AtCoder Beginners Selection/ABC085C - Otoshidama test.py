# MLE 誤り

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

from sklearn.utils.extmath import cartesian
import numpy as np

n,y = map(int,input().split())

arrays = cartesian((range(0,n+1),range(0,n+1),range(0,n+1)))

filter0 = arrays.sum(axis=1) == n
arrays = arrays[filter0]

osatu = np.array([10000,5000,1000])

otosidama = (arrays*osatu).sum(axis=1)

if not y in otosidama:
    x,y,z = (-1,-1,-1)
else:
    filter1 = np.where(otosidama == y)
    x,y,z = tuple(arrays[filter1][0])

print("{} {} {}".format(x,y,z))