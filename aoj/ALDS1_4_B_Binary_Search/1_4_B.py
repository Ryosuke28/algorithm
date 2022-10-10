# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_B

# pythonのbisectモジュールを使用して解くことも可能
# bisect_left(S, key) で、昇順を保ったままSにkeyを挿入する際のindexが得られる
# その位置の要素S[index]がkeyと一致するかどうかを調べる

def binary_search(ary, n, key):
    left = 0
    right = n
    while left < right:
        center = int((left + right) / 2)
        if ary[center] == key:
            return True
        elif ary[center] < key:
            left = center + 1
        else:
            right = center
    return False


n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

ans = 0
for key in T:
    if binary_search(S, n, key):
        ans += 1

print(ans)
