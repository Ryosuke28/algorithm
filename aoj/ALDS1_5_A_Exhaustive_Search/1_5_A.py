n = int(input())
A = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))
list = set()


def solve(i, total):
    list.add(total)
    if i == n:
        return True

    solve(i+1, total)
    solve(i+1, total+A[i])


solve(0, 0)
for length in m:
    print('yes' if length in list else 'no')


# 以下、別解


def solve_minus(i, rest):
    if rest == 0:
        return True
    elif rest < 0 or i >= n:
        return False

    res = solve(i+1, rest) or solve(i+1, rest - A[i])
    return res


for length in m:
    print('yes' if solve_minus(0, length) else 'no')
