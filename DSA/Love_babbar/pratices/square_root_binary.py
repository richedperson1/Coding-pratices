def square_root(ele):
    low = 0
    high = ele-1
    while low <= high:
        mid = (low+high)//2
        if mid*mid == ele:
            return mid
        elif mid*mid > ele:
            high = mid-1
        else:
            low = mid+1

    return -1


print(square_root(625))