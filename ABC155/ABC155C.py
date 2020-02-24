from collections import Counter

n = int(input())
S = []
for _ in range(n):
    S.append(input())  # S += [input()] とも書ける

# 要素数チェック
counter = Counter(S)
# 要素数最大の要素を全て取得する->リスト
mostnum = 0
ans = []
for c in counter.most_common():
    if mostnum <= c[1]:
        mostnum = c[1]
        ans.append(c[0])
    else:
        break
# リストを辞書順に並び替える
ans.sort()
# リストを改行で出力
for a in ans:
    print(a)