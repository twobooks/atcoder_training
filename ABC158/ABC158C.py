from math import ceil

a,b = map(int,input().split())

a_btm = ceil(a*100/8)
a_top = int((a+1)*100/8)

b_btm = b*10
b_top = (b+1)*10 -1

minn = min(a_btm,a_top,b_btm,b_top)
maxx = max(a_btm,a_top,b_btm,b_top)

ans = -1
for i in range(minn,maxx+1):
    if int(i*0.08)==a and int(i*0.1)==b:
        ans = i
        break

print(ans)

# ans = -1
# for aa in range(a_btm,a_top):
#     for bb in range(b_btm,b_top):
#         if aa == bb:
#             ans = aa
#             break
#     break

