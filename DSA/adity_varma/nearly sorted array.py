arr = [3, 2, 10, 4, 40,39,45,69]
n = len(arr)
ele = 69

low = 0
high = n-1

while low<=high:
    mid = (low+high)//2
    if arr[mid]==ele:
        print(mid)
        exit()

    elif mid-1>=low and arr[mid-1]==ele:
        print(mid-1)
        exit()
    elif mid+1<=high and arr[mid+1]==ele:
        print(mid+1)
        exit()

    elif arr[mid]<ele:
        low = mid+2
    else:
        high = mid-2

print("NOt preset")