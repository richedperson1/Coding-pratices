arr = [10,20,30,40]
n = len(arr)
m = 2


def ispossible(arr, n, m, mid):
    pagesum = 0
    student = 1
    for i in range(n):
        if pagesum+arr[i] <= mid :
            pagesum += arr[i]
        else:
            student += 1
            if student > m or arr[i] > mid:
                return False
        pagesum = arr[i]
    return True


def allocation(arr, n, m):
    low = 0
    high = sum(arr)
    ans = -1
    while low <= high:
        mid = (low+high)//2
        if ispossible(arr, n, m, mid):
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans

print(allocation(arr,n,m))