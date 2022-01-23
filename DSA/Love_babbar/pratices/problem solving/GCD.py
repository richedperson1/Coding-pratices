def modularExponentiation(x, n, m):
    # Write your code here.
    res = 1
    while n > 0:
        if x & 1:
            res = (res*x) % n
        x = (x*x) % m

        n = n >> 1
    return res

tt = set([5,6,8,6,3,8])