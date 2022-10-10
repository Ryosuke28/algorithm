import sys
from collections import deque


def dfs_init(n):
    global D, F, color, time
    D, F, color = [None] * n, [None] * n, [0] * n
    time = 0


def calc_stack(u, V, n):
    global D, F, color, time

    dq = deque()

    dq.append(u)
    time += 1
    D[u] = time

    while len(dq) != 0:
        u = dq[-1]
        if len(V[u]) != 0:
            v = V[u].pop(0)
            if color[v] == 0:
                time += 1
                D[v] = time
                color[v] = 1
                dq.append(v)
        else:
            dq.pop()
            color[u] = 2
            time += 1
            F[u] = time


def dfs_recursive(u):
    global V, D, F, color, time

    color[u] = 1
    time += 1
    D[u] = time

    for v in V[u]:
        if color[v] == 0:
            dfs_recursive(v)
    color[u] = 2
    time += 1
    F[u] = time


def main():
    global V

    n = int(input())
    V = []
    for _ in range(n):
        id, num, *vs = map(int, input().split())
        V.append([v-1 for v in vs])

    dfs_init(n)

    # for u in range(n):
    #     if color[u] == 0:
    #         calc_stack(u, V, n)

    for u in range(n):
        if color[u] == 0:
            dfs_recursive(u)
    for i in range(n):
        print(f'{i+1} {D[i]} {F[i]}')


input = sys.stdin.readline
main()
