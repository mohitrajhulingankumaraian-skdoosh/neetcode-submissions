class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        num_set = set(nums)
        for n in nums:
            if n-1 not in num_set:
                cnt = 0
                while n in num_set:
                    cnt += 1
                    #num_set.remove(n)
                    n += 1
                max_len =max(cnt, max_len)
        
        return max_len