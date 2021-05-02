SX,SY,GX,GY = map(int,input().split())

Y = GY + SY
X = GX - SX

katamuki = Y/X

ans = SY/katamuki +SX
print(ans)

