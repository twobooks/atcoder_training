N = int(input())
Q = int(input())

# 行番号を記憶する配列
# AijはN*(i-1)+j-1なので0~1が入ってる
row_num = list(range(N))
# 列番号を記憶する配列
# AijはN*(i-1)+j-1なので0~1が入ってる
col_num = list(range(N))

# 転置されているか否かを管理する変数。転置されていれば要素はN*j+iになる
trans_flag = False

for q in range(Q):
    query = list(map(int,input().split()))
    # クエリタイプ
    t = query[0]
    # クエリタイプ3以外はA、Bが後に続く。0始まりにしておく
    if t != 3:
        A,B = query[1:3]
        A -= 1
        B -= 1
    
    if t == 1:
        row_num[A],row_num[B] = row_num[B],row_num[A]
    elif t == 2:
        col_num[A],col_num[B] = col_num[B],col_num[A]
    elif t == 3:
        row_num,col_num = col_num,row_num
        trans_flag = not trans_flag
    else:
        if trans_flag is False:
            print(row_num[A]*N + col_num[B])
        else:
            print(col_num[B]*N + row_num[A])