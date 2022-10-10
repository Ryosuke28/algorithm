import sys


def prim(n, V):
    global color, d, p

    # 頂点0からスタート
    d[0] = 0
    p[0] = 0

    while True:
        mincost = 2001
        for i in range(n):  # 頂点i。0~n-1まで
            if color[i] != 2 and d[i] < mincost:  # 頂点1がMSTに属していない and ある頂点の中で最小のもの
                mincost = d[i]  # 最小の辺の重みをmincostに代入
                u = i  # 追加する頂点i を u に代入

        if mincost == 2001:
            break

        color[u] = 2  # 頂点i(u)をMST追加済みにする

        for v in range(n):
            if color[v] != 2 and V[u][v] != -1:  # uとvの間に辺がある:
                if V[u][v] < d[v]:  # MSTの頂点から外部の頂点への重み
                    d[v] = V[u][v]
                    p[v] = u
                    color[v] = 1


def main():
    global color, d, p

    n = int(input())
    V = []
    for _ in range(n):
        V.append(list(map(int, input().split())))

    # 全ての頂点uについて、color[u]=WHITE、d[u]=INFTYで初期化
    color = [0] * n
    d = [2001] * n  # d[v]:頂点vにとってMSTと繋がる最小の辺の重み
    p = ['?'] * n  # p[v]:vにとってd[v]でつながっている頂点の番号

    prim(n, V)
    print(sum(d))


input = sys.stdin.readline
main()
