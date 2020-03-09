n = int(input())

list99 = set()

for i in range(1,10):
    for j in range(1,10):
        list99.add(i*j) 

if n in list99:
    print("Yes")
else:
    print("No")
