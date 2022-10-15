from math import gcd

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [gcd(a[0], b[0]), gcd(a[1], b[1])]
d = [gcd(a[0], b[1]), gcd(a[1], b[0])]
k = c if c[0] * c[1] > d[0] * d[1] else d
print(' '.join(map(str, k)))