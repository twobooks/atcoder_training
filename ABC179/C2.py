N = int(input())

ans = 0

for A in range(1,N):
    # A*B > N ならans+=1,加算すべき数はA*1からA*(N-1)/Aまでの組み合わせの個数
    ans += (N-1)//A

print(ans)