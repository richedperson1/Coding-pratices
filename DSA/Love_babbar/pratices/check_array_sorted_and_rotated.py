# arr = [1,2,3,4,5]
# cnt = 0
# n = len(arr)
# for i in range(1):
#     if arr[i-1]>arr[i]:
#         cnt+=1


# # if arr[n-1]>arr[0]:
# #     cnt+=1

# if cnt==1:
#     print(True)
# else:
#     print(False)
def check( nums: list[int]) -> bool:
    cnt = 0
    n = len(nums)
    total = 0
    local = nums[0]
    for i in range(n):
        if local==nums[i]:
            total+=1
        if nums[i-1]>nums[i]:
            cnt+=1
    
    if total==n:
        return True
    return cnt==1,total

print(check([6,6,6,6,6,6,5]))