N,K = list(map(int,input().split()))
S = input()

nex = [[len(S)]*26 for i in range(len(S)+1)]
for i in range(len(S)-1,-1,-1):
	for j in range(26):
		if ord(S[i]) - ord('a') == j:
			nex[i][j] = i
		else:
			nex[i][j] = nex[i + 1][j]

# Step #3. 一文字ずつ貪欲に決める
Answer = ""
CurrentPos = 0
for i in range(1,K+1):
    for j in range(26):
        NexPos = nex[CurrentPos][j]
        MaxPossibleLength = len(S) - NexPos - 1 + i
        if (MaxPossibleLength >= K):
            Answer += chr(ord('a') + j)
            CurrentPos = NexPos + 1
            break

# Step #4. 出力
print(Answer)