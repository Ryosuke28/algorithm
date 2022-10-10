import sys
from collections import deque


def bfs(u):
    global colors, dq

    if colors[u] == -1:
        colors[u] = color

        for v in V[u]:
            if colors[v] == -1 and v not in dq:
                dq.append(v)

    if len(dq) != 0:
        bfs(dq.popleft())


def bfs_que(u):
    global colors, dq

    dq.append(u)
    colors[u] = color

    while len(dq) != 0:
        now = dq.popleft()
        for v in V[now]:
            if colors[v] == -1:
                dq.append(v)
                colors[v] = color


def dfs(u):
    global colors, dq

    colors[u] = color

    for v in V[u]:
        if colors[v] == -1:
            dfs(v)


def main():
    global V, colors, color, dq

    n, m = map(int, input().split())
    V = [[] for _ in range(n)]
    for _ in range(m):
        s, t = map(int, input().split())
        V[s].append(t)
        V[t].append(s)

    colors = [-1] * n
    dq = deque()
    color = 0
    for i in range(n):
        if colors[i] == -1:
            # bfs(i)
            bfs_que(i)
            # dfs(i)
            color += 1

    q = int(input())
    for _ in range(q):
        s, t = map(int, input().split())
        if colors[s] == colors[t]:
            print('yes')
        else:
            print('no')


input = sys.stdin.readline
main()
