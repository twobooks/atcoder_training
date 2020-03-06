import math

import numpy as np
import scipy as scp

# 演算子
a + b         # 加算
a - b         # 減算
a * b         # 乗算
a / b         # 除算
a % b         # a を b で割った余り
a ** b        # a の b 乗
a // b        # 切り捨て除算
divmod(x,y)   # 商と余りを返す

# ビット演算とか
a >> b        # 右シフト
a << b        # 左シフト
a & b         # 論理積(and) 1桁毎の掛け算
a | b         # 論理和(or)  1行毎の足し算で1以上は1
a ^ b         # 排他的論理和(xor) 1行毎の足し算で1以上は0
~a            # 反転
format(a,"04b") # intを4桁で2進数のstrに変換
bin(a)        # intを2進数のstrに変換。頭に"0b"のプレフィックスが付く
bin(a).count("1") # 2進数表記した時の1の数をカウントする




# コンソールのクリア
os.sysytem("cls")

# lcm() 最小公倍数を返すやつ
def lcm(x:int, y:int)->int:
    """
    return Least common multiple (最小公倍数)
    """
    return (x * y) // gcd(x, y)

# 組合せの計算
def comb(n:int,k:int,MOD:int):
    """return nCk (mod MOD)
    """
    nCk = 1
    # n!/(n-k)!
    for i in range(n-k+1, n+1):
        nCk *= i
        nCk %= MOD
    # 1/k!
    for i in range(1,k+1):
        nCk *= pow(i,MOD-2,MOD)
        nCk %= MOD
    return nCk

# 繰返し二乗法
# pythonだと標準関数でOK
pow(n,p,mod) # n:底、p:指数、mod:mod
pow(n,mod-2,mod) # mod:modでのnの逆元

# 文字列の分割
import re
st = "???a?bb????ccc?"
re.split("[a-z]",st)    #正規表現で指定してsplitできる
max([len(i) for i in re.split("\?",st)])  #split後の文字数の最大値を求める

# continue,break,exit()
import sys
while True:
  for i in range(10):
    if i ==3:
      continue # 以降の処理はスルーされて処理はfor文に戻る
    # elif i == 7:
    #   break # forループ自体(else文部分も含めて)が終了する
    else:
      print(i)
  else:   # forループのイテレータが無くなったら実行されるforループのelse文
    print("done")
    exit()  # atcoderだとwhileループも含めて処理全終了になる。
            # atcoder以外だとsys.exit()が無難。多分エラー出るけど
  break # forループ終了後に実行されるwhileのbreak。whileループが終了する。
    



