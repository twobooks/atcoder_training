N = int(input())

trues = 1
falses = 1

for i in range(N):
    kigou = input()
    if kigou=="AND":
        trues = trues
        falses = trues + falses*2 
    else:
        trues = trues*2 + falses
        falses = falses

print(trues) 