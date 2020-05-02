# from math import factorial,sqrt,ceil,gcd
# from itertools import permutations as permus
from collections import deque,Counter
# import re
# from functools import lru_cache # 簡単メモ化 @lru_cache(maxsize=1000)
# from decimal import Decimal, getcontext
# # getcontext().prec = 1000
# # eps = Decimal(10) ** (-100)

# import numpy as np
# import networkx as nx
# from scipy.sparse.csgraph import shortest_path, dijkstra, floyd_warshall, bellman_ford, johnson
# from scipy.sparse import csr_matrix
# from scipy.special import comb

# slist = "abcdefghijklmnopqrstuvwxyz"
S = input()

cnt = Counter(S)

flg = max(cnt["a"],cnt["b"],cnt["c"]) - min(cnt["a"],cnt["b"],cnt["c"])

ans = "YES"
if flg>1:
    ans = "NO" 
    
print(ans)
