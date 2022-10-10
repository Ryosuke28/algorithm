n = int(input())
A = list(map(int, input().split()))


def merge(ary, left, mid, right):
    global count
    L = ary[left:mid] + [1000000001]
    R = ary[mid:right] + [1000000001]

    i, j = 0, 0
    for k in range(left, right):
        if L[i] <= R[j]:
            ary[k] = L[i]
            i += 1
        else:
            ary[k] = R[j]
            j += 1
        count += 1


def merge_sort(ary, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        merge_sort(ary, left, mid)
        merge_sort(ary, mid, right)
        merge(ary, left, mid, right)


count = 0
merge_sort(A, 0, n)

print(*A)
print(count)
