class Solution:
    def left_binary(self,arr,low,high,k):
        ans = -1
        while low <=high:
            mid = (low+high)//2
            if arr[mid]==k:
                ans = mid
                high = mid-1

            elif arr[mid]>k:
                high = mid-1
            else:
                low = mid+1
        return ans
    def right_binary(self,arr,low,high,k):
        ans = -1
        while low <=high:
            mid = (low+high)//2
            if arr[mid]==k:
                ans = mid
                low = mid+1

            elif arr[mid]>k:
                high = mid-1
            else:
                low = mid+1
        return ans
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        if n==0:
            return [-1,-1]
        elif nums[0]==nums[-1]==target:
            return [0,n-1]
        else:
            n = len(nums)-1
            left = self.left_binary(nums,   0,n,target)
            right = self.right_binary(nums, 0,n,target)
            return ([left,right])

rutvik = Solution()
print(rutvik.searchRange( [5],8))