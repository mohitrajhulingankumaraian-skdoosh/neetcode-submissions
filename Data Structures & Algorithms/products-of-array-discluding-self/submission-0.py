class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        prod = 1
        ans[-1] = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            ans[i] = nums[i]*ans[i+1]
        
        for i in range(len(nums)-1):
            ans[i] = prod*ans[i+1]
            prod *= nums[i]

        ans[-1] = prod
        
        return ans
        