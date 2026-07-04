class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (i +j)//2
            if nums[mid] < nums[mid - 1] and nums[mid] < nums[(mid+1)%len(nums)]:
                return nums[mid]
            
            elif nums[mid] > nums[j]:
                i = mid+1
            else:
                j = mid - 1
        
        return -1