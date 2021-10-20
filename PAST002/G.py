from collections import deque,Counter
from string import ascii_lowercase

Q = int(input())
que = deque()

ans = 0
for q in range(Q):
    # 文字と数字が混じっているので一旦文字でinputを受け取る
    values = input().split()
    if values[0] == "1":
        # クエリ1の処理
        c = values[1]
        x = int(values[2])
        que.append([c,x])
    else:
        d = int(values[1])
        
        # cnt = {}
        # for c in ascii_lowercase:
        #     cnt[c] = 0
        cnt = Counter()

        while d>0 and len(que)>0:
            c,x = que[0]
            if d>=x:
                d -= x
                cnt[c] += x
                que.popleft()
            else:
                que[0][1] -= d
                cnt[c] += d
                d = 0

        ans = 0
        # for c in ascii_lowercase:
        #     ans += cnt[c]**2
        for c in cnt:
            ans += cnt[c]**2

        print(ans)