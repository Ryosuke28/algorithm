import sys


def dijkstra(n, M):
    global color, d, p

    # 頂点0からスタート
    d[0] = 0
    p[0] = 0

    while True:
        mincost = 10000000
        for i in range(n):  # 頂点i。0~n-1まで
            if color[i] != 2 and d[i] < mincost:  # 頂点iが訪問済み頂点Sに属していない and ある頂点の中で最小のもの
                mincost = d[i]  # 最小の辺の重みをmincostに代入
                u = i  # 追加する頂点i を u に代入

        if mincost == 10000000:
            break

        color[u] = 2  # 頂点i(u)をMST追加済みにする

        for v in range(n):
            if color[v] != 2 and M[u][v] != 10000000:  # uとvの間に辺がある:
                if d[u] + M[u][v] < d[v]:  # vへu経由の経路が経由せずよりコストが低い場合、コストを更新
                    d[v] = d[u] + M[u][v]
                    p[v] = u
                    color[v] = 1


def main():
    global color, d, p

    n = int(input())
    M = [[10000000] * n for _ in range(n)]
    for _ in range(n):
        line = list(map(int, input().split()))
        for i in range(line[1]):
            M[line[0]][line[i*2+2]] = line[i*2+3]

    # 全ての頂点uについて、color[u]=WHITE、d[u]=INFTYで初期化
    color = [0] * n
    d = [10000000] * n  # d[v]:頂点vにとってMSTと繋がる最小の辺の重み
    p = ['?'] * n  # p[v]:vにとってd[v]でつながっている頂点の番号

    dijkstra(n, M)
    for (i, cost) in enumerate(d):
        print(*[i, cost])


input = sys.stdin.readline
main()
