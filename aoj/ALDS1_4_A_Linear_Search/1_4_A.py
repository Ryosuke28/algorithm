# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_A
# python のメソッドを使用する場合、 result = key in S で良い

def search(ary, n, key):
    i = 0
    ary.append(key)
    while ary[i] != key:
        i += 1
    ary.pop()
    return i != n


n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

ans = 0
for key in T:
    if search(S, n, key):
        ans += 1

print(ans)
