# input
# 文字列S,1≦S≦10^5
# 操作
# Tが空文字列である状態から始め、以下の操作を好きな回数繰り返すことで S=T とすることができるか判定。
# T の末尾に dream dreamer erase eraser のいずれかを追加する。
#
# output
# S=T  とすることができる場合 YES を、そうでない場合 NO を出力

s = input()

t1 = ["dream","erase"]
t2 = ["eraser"]
t3 = ["dreamer"]

result = ""
while len(s) !=0:
    if len(s)<5:
        result = "NO"
        break
    else:
        if s[-5:] in t1:
            s = s[:-5]
        elif s[-6:] in t2:
            s = s[:-6]
        elif s[-7:] in t3:
            s = s[:-7]
        else:
            result = "NO"
            break

if len(s)==0:
    result = "YES"

print(result)