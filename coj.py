'''def US(n, n2):
    if n == 10: return 1
    if n == 0: return 0
    n2 += US(n / 10, n2)
    return n2 + n % 10
'''
def US(n):
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
    T -= 1
