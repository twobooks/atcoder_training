def main():
    N, M = list(map(int, input().split()))

    GCPs = []  # 出す手
    for i in range(2 * N):
        GCPs.append(input())
    # 勝利数管理, [勝利数,member番号]
    winCount = []
    for i in range(2 * N):
        winCount.append([0, i])
    # 対決順用
    taisenyou = sorted(winCount, key=sortorder, reverse=True)
    # print("winCount", winCount)
    # print("taisenyou", taisenyou)
    for m in range(M):
        for i in range(1, N + 1):
            _, id1 = taisenyou[2 * i - 1-1]
            _, id2 = taisenyou[2 * i-1]
            janken(id1, id2, m, GCPs, winCount)
        taisenyou = sorted(winCount, key=sortorder, reverse=True)
        # print("winCount", winCount)
        # print("taisenyou", taisenyou)

    for i in range(2 * N):
        print(taisenyou[i][1]+1)


def sortorder(x):
    tmp = [x[0], x[1] * -1]
    return tmp


def janken(id1, id2, M, GCPs, winCount):
    if GCPs[id1][M] == GCPs[id2][M]:
        pass
    elif GCPs[id1][M] == "G":
        if GCPs[id2][M] == "C":
            winCount[id1][0] += 1
        else:
            winCount[id2][0] += 1
    elif GCPs[id1][M] == "C":
        if GCPs[id2][M] == "P":
            winCount[id1][0] += 1
        else:
            winCount[id2][0] += 1
    elif GCPs[id1][M] == "P":
        if GCPs[id2][M] == "G":
            winCount[id1][0] += 1
        else:
            winCount[id2][0] += 1
    else:
        pass


main()
