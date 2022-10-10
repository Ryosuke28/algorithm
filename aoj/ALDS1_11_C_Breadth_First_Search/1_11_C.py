import sys
from collections import deque


def bfs_init(n):
    global d, dq

    d = [-1] * n
    dq = deque()


def bfs(u):
    global d, dq

    distance = d[u] + 1

    for v in V[u]:
        if d[v] == -1:
            dq.append(v)
            d[v] = distance

    if len(dq) != 0:
        bfs(dq.popleft())


def bfs_text():
    global d

    d[0] = 0
    dq.append(0)

    while len(dq) != 0:
        u = dq.popleft()
        distance = d[u] + 1

        for v in V[u]:
            if d[v] == -1:
                d[v] = distance
                dq.append(v)


def main():
    global V

    n = int(input())
    V = []
    for _ in range(n):
        id, num, *vs = map(int, input().split())
        V.append([v-1 for v in vs])

    bfs_init(n)

    # d[0] = 0
    # bfs(0)

    bfs_text()

    for i in range(n):
        print(f'{i+1} {d[i]}')


input = sys.stdin.readline
main()
