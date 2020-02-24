import numpy as np

n = int(input())
arrA = np.array(input().split(),dtype=np.int64)

filter = (arrA % 2 == 0)
if len(arrA[filter])==0:
    ans = "APPROVED"
else:
    for i in arrA[filter]:
        if i%3==0 or i%5==0:
            ans = "APPROVED"
        else:
            ans = "DENIED"
            break

# APPROVED or DENIED
print(ans)