N =int(input())

if N == 1:
    print(1)
    exit()

ansl = []
ansr =[]
for i in range(1,N+1):
    if i**2>N:
        break
    if i**2 == N:
        ansl.append(i)
        continue
    if N%i==0:
        ansl.append(i)
        ansr.append(N//i)

print(*ansl,*ansr[::-1],sep="\n")