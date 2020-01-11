a = int(input())
b = int(input())
c = int(input())
x = int(input())

x50 = x//50
x100 = x//100
x500 = x//500

count = 0

if x > 500*a+100*b+50*c:
    pass
elif x50 % 2 == 1 and c==0:
    pass
elif x100 % 5 != 0 and c==0 and b==0:
    pass
else:
    for gohyaku in range(a+1):
        for hyaku in range(b+1):
            for gojuu in range(c+1):
                if x == gojuu*50 + hyaku*100 + gohyaku*500:
                    count += 1
print(count)