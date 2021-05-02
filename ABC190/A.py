A,B,C = map(int,input().split())

sente = "Takahashi"
gote = "Aoki"

if C ==1:
    A,B = B,A
    sente,gote = gote,sente
    # gote = "Takahashi"
    # sente = "Aoki"

if A>B:
    print(sente)
if A<=B:
    print(gote)
