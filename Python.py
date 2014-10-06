'''def US(n, n2):
    if n == 10: return 1
    if n == 0: return 0
    n2 += US(n / 10, n2)
    return n2 + n % 10
'''
'''def US(n):
    if n < 10:
        return n
    num = 0
    while n > 0:
        num += n % 10
        n /= 10
    return num

T = int(raw_input())
while T > 0:
    N = int(raw_input())
    a = 10
    while a > 9:
        a = US(N)
        N = a
    print a
    T -= 1'''

a, b, c = 0, 0, 0
while True:
    c += 1
    y = raw_input()
    y2 = y.split(' ')
    a, b = int(y2[0]), int(y2[1])
    if a == 0 and b == 0:
        break
    x, c2, s, s2 = 0, 0, 1, 1
    i = 0
    while x + 1 < b:
        x += i
        while s < x + 1:
            s2 += 1
            s = s2 * s2
        if x + 1 > a and x + 1 < b and x + 1 == s:
            c2 += 1
        i += 1
    print "Case {0}: {1}".format(c, c2)
