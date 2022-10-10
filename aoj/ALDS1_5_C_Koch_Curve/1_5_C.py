import math

n = int(input())
angle = math.radians(60)
sin60 = math.sin(angle)
cos60 = math.cos(angle)


def koch_curve(i, p1, p2):
    if i == n:
        return True
    s = [
        p1[0] * 2/3 + p2[0] * 1/3,
        p1[1] * 2/3 + p2[1] * 1/3
    ]
    t = [
        p1[0] * 1/3 + p2[0] * 2/3,
        p1[1] * 1/3 + p2[1] * 2/3
    ]
    u = [
        (t[0]-s[0])*cos60 - (t[1]-s[1])*sin60 + s[0],
        (t[0]-s[0])*sin60 + (t[1]-s[1])*cos60 + s[1]
    ]

    koch_curve(i+1, p1, s)
    print(*s)
    koch_curve(i+1, s, u)
    print(*u)
    koch_curve(i+1, u, t)
    print(*t)
    koch_curve(i+1, t, p2)


print(*[0, 0])
koch_curve(0, [0, 0], [100, 0])
print(*[100, 0])
