N = int(input())

def check10(num):
    if "7" in str(num):
        return True
    else:
        return False

def check8(num):
    if "7" in oct(num):
        return True
    else:
        return False


ans = 0
for i in range(1,N+1):
    if check10(i):
        ans += 1
        continue
    if check8(i):
        ans += 1
        continue

print(N-ans) 