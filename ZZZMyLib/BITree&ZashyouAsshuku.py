import sys
from heapq import *
import numpy as np
import numba
from numba import njit, b1, i1, i4, i8, f8

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=' ')

def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=' ')

# BITの構築ぽい
@njit
def build(raw_data):
    shape = raw_data.shape
    N = len(raw_data)
    bit = np.zeros((N + 1, ) + shape[1:], np.int64)
    for i in range(1, N + 1):
        bit[i] += raw_data[i - 1]
        j = i + (i & (-i))
        if j < len(bit):
            bit[j] += bit[i]
    return bit


# BITのi-1までの合計
@njit
def get_sum(bit, i):
    """sum on [0, i)"""
    s = 0
    while i:
        s += bit[i]
        i -= i & -i
    return s

# BITのiにxを加える
@njit
def add(bit, i, x=1):
    assert 0 <= i < len(bit) - 1
    i += 1
    while i < len(bit):
        bit[i] += x
        i += i & -i


@njit
def find_kth_element(bit, k):
    assert k > 0
    N = len(bit)
    x, sx = 0, 0
    dx = 1
    while 2 * dx < N:
        dx *= 2
    while dx:
        y = x + dx
        if y < N:
            sy = sx + bit[y]
            if sy < k:
                x, sx = y, sy
        dx //= 2
    return x

@njit((i8, i8, i8[:], i8[:]), cache=True)
def main(L, Q, C, X):
    V = X.copy()
    V = np.append(V, 0)
    V = np.append(V, L)
    V = V[np.argsort(V, kind='mergesort')]
    V = np.unique(V)
    X = np.searchsorted(V, X)
    bit = np.zeros(len(V) + 10, np.int64)
    add(bit, 0, 1)
    add(bit, len(V) - 1, 1)

    for q in range(Q):
        c, x = C[q], X[q]
        if c == 1:
            add(bit, x, 1)
        else:
            k = get_sum(bit, x)
            n = find_kth_element(bit, k)
            m = find_kth_element(bit, k + 1)
            print(V[m] - V[n])

# 一行取得してnumpy.arrayで受け取る。整数L、Qを取得
L, Q = from_readline()
# 残り全部取得してnumpy.arrayで受け取る。reshapeしてから転置して数列CとXを得る
C, X = from_read().reshape(Q, 2).T

# main(L, Q, C, X)

V = X.copy() # XのコピーをVとする。Xは切られた個所や、長さの問い合わせの基準点のQuery問い合わせの順の配列
V = np.append(V, 0) # Vに0点を追加
V = np.append(V, L) # VにL点を追加
V = V[np.argsort(V, kind='mergesort')] # Vを昇順に並び替え
V = np.unique(V) # Vの重複値を削除
# np.searchsorted(A,B)はソート済み列Aに対してB(int,arrいずれもOK)を
# どこに入れればソート維持したままでいけるかをindexで返す。デフォルトはleft。2分探索してるぽい。
# いわゆる座標圧縮？
X = np.searchsorted(V, X) # VとXの要素は同じなので、Xの各要素はVのどのindexに対応しているかの配列を取得してXにしている。
bit = np.zeros(len(V) + 10, np.int64) # BIT用の配列用意
add(bit, 0, 1) # BITの0要素に1加えてる。多分0の切れ目(V[0])に対応するものとして1加えてる
add(bit, len(V) - 1, 1) # BITのlen(V)-1要素に1加えてる。多分Lの切れ目0(V[len(V)-1])に対応するものとして1加えてる

for q in range(Q): # Query処理
    c, x = C[q], X[q] # c,x取得. xは座標圧縮後のVのindexになってる
    if c == 1:
        add(bit, x, 1) # BITに元々の切れ目xに対応するVのindexに1を加える
    else:
        # 元々の切れ目xに対応するVのindexまでのBIT上の合計値を取得してる。
        # BITには1しか入ってないので要は元々の切れ目xに対応するVのindexまでの切れ目入った要素の個数を取得してる
        k = get_sum(bit, x)
        n = find_kth_element(bit, k) # BITを探索してBITに入ってるk個目の要素はＶのindexでいうと何番目かを取得
        m = find_kth_element(bit, k + 1) # 同じ
        print(V[m] - V[n])

# 恐らくC++のsetを用いた平衡二分木探索の代わりにBITを用いている。
# lower_bound,upper_boundの代わりにfind_kth_element(bit, k)、find_kth_element(bit, k+1)してるみたい