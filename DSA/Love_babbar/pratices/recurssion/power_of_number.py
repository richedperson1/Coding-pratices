def power(a, b):
    if b == 0:
        return 1

    if b == 1:
        return a

    ans = power(a, b//2)
    print(b)
    
    if b & 1:
        ans = a*ans*ans
        return ans
    else:
        return ans * ans


power(2,9)