# 入力
# N
# a1,a2,a3 ... an
# 
# 出力
# Aliceが先にanからカードを取る、次にBobがカードを取る。
# 両者が最適な戦略を取った時, Alice は Bob より何点多く取るかを出力してください.

import numpy as np

n = int(input())
card = np.array(input().split(),dtype=np.int64)

if n == 1:
    score = card[0]
else:
    card.sort()
    card = card[::-1]
    alice_score = card[0::2].sum()
    bob_score = card[1::2].sum()
    score = alice_score - bob_score

print(score)