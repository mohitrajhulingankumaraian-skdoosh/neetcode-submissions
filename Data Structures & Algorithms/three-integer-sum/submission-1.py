class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        i = 0
        while i < len(nums)-2:
            j, k = i+1, len(nums)-1
            while j < k:
                if nums[j] + nums[k] == -nums[i]:
                    ans.append((nums[i],nums[j],nums[k]))
                    j, k = j+1, k-1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                elif nums[j] + nums[k] > -nums[i]:
                    k -= 1
                else:
                    j += 1
            i += 1
            while i < len(nums)-2 and nums[i] == nums[i-1]:
                i += 1
        
        return ans
