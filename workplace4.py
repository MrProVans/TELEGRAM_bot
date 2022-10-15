def dev1(n, m):
    global y0, x0, dx, dy, ck, part2, arr
    arr[y0][x0] = 1
    nx, ny = x0 + dx, y0 + dy
    if part2 <= nx < n - part2 and part2 <= ny < m - part2 and not arr[ny][nx]:
        x0, y0 = nx, ny
    else:
        dx, dy = dy, -dx
        x0, y0 = x0 + dx, y0 + dy
    return x0, y0


def dev2():
    global cordx1, cordy1, post1, flag1
    if cordy1 == y - 1 and cordx1 == 0:
        cordy1 -= 1
    elif (cordy1 == 0 or cordy1 == y - 1) and flag1:
        cordx1 += 1
        post1 *= -1
        flag1 = False
    else:
        flag1 = True
        cordy1 += post1
    return cordx1, cordy1


y, x, k = map(int, input().split())
cordx1, cordy1 = 0, y - 1
post1 = -1
flag1 = True
part2 = 0
ck = 0
dx, dy = 1, 0
x0, y0 = 0, y - 1
arr = [[None] * x for _ in range(y)]
arr[y - 1][0] = 1
a = [[0 for i in range(x)] for j in range(y)]
a[y - 1][0] = 3
t = [1]
for i in range(1, x * y):
    s = dev1(x, y)
    h = 0
    if a[s[1]][s[0]] == 2:
        a[s[1]][s[0]] = 3
        h += 1
    else:
        a[s[1]][s[0]] = 1
    s = dev2()
    if a[s[1]][s[0]] == 1:
        a[s[1]][s[0]] = 3
        h += 1
    else:
        a[s[1]][s[0]] = 2
    t.append(t[-1] + h)
u = []
for i in input().split():
    u.append(str(t[int(i) - 1]))
print(' '.join(u))
