class segtree:
    """
    Segment tree\\
    Store value as object type and optional function for binary operarion.\\
    "get" function return a value by binary operarion result. O(logN)\\
    "update" function update tree's a value. O(logN)

    Attributes
    ----------
    n : int
        Number of elements
    identity element_func : func
        Identity_element for initialization.\\
        If operator is * and identiry element is e, e * A = A and A * e = A.
    binary_operation_func : func
        Function for binary operation x and y.\\
        Function must have associative law.\\
        If operator is *, (A * B) * C = A * (B * C).

    Methods
    -------
    update(i, x)
        Update tree[i] value to x
    get(a, b)
        Get value from [a, b).\\
        Include a but not include b, return a merged value.
    """

    def __init__(self, n: int, identity_element_func, binary_operation_func):
        """
        Constructer(Initialize parameter in this class)

        Parameters
        ----------
        n : int
            Number of elements
        identity_element_func : func
            Identity element for initialization\\
            If operator is * and identiry element is e, e * A = A and A * e = A
        binary_operation_func : func
            Function for binary operation x and y.\\
            Function must have associative law.\\
            If operator is *, (A * B) * C = A * (B * C)
        """
        self.identity = identity_element_func
        self.binary = binary_operation_func
        self.offset = 1 << (n - 1).bit_length()  # offsetはnより大きい2の冪数
        self.tree = [self.identity() for _ in range(self.offset << 1)]

    @classmethod
    def from_array(cls, arr, identity_element_func, binary_operation_func):
        """Initialize from array"""
        ins = cls(len(arr), identity_element_func, binary_operation_func)
        ins.tree[ins.offset:ins.offset + len(arr)] = arr
        for i in range(ins.offset - 1, 0, -1):
            lch = i << 1
            ins.tree[i] = binary_operation_func(
                ins.tree[lch], ins.tree[lch + 1])
        return ins

    def update(self, index: int, x: int):
        """
        Overwrite segment-tree's a value and update parent nodes.
        This method updates the value to the new value regardless of the previous value.

        Parameters
        ----------
        index : int
            index of update value
        x     : int
            new value
        """
        index += self.offset
        self.tree[index] = x
        while index > 1:
            index >>= 1  # 右ビットシフトで親ノードのインデックスへ移動
            lch = index << 1
            self.tree[index] = self.binary(self.tree[lch], self.tree[lch + 1])

    def get(self, left: int, right: int) -> int:
        """
        Get a specific value by result of binary operation from interval [left, right).

        Parameters
        ----------
        left, right : int
            Index of interval.\\
            This is hald open interval, this interval include left but not right.
        """
        result_l = self.identity()
        result_r = self.identity()
        left += self.offset
        right += self.offset
        while left < right:
            if left & 1:
                result_l = self.binary(result_l, self.tree[left])
                left += 1
            if right & 1:
                right -= 1
                result_r = self.binary(self.tree[right], result_r)
            left >>= 1
            right >>= 1

        return self.binary(result_l, result_r)

L, Q = map(int, input().split())
query = [list(map(int, input().split())) for _ in range(Q)]
INF = 10 ** 18

# 座標圧縮
X = set()
x_to_i = {}
for c, x in query:
    X.add(x)
X = sorted(X)
for i, x in enumerate(X):
    x_to_i[x] = i

# 線xiを含む木材の右端のxを返すセグ木
search_right_end = segtree(len(X), lambda: INF, min)
search_right_end.update(len(X) - 1, L)
# 線xiを含む木材の左端のxを返すセグ木
search_left_head = segtree(len(X), lambda: 0, max)
search_left_head.update(0, 0)
for c, x in query:
    i = x_to_i[x]
    if c == 1:
        search_right_end.update(i, x)
        search_left_head.update(i, x)
    else:
        right = search_right_end.get(i, len(X))
        left = search_left_head.get(0, i)
        print(right - left)