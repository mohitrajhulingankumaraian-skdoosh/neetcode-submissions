class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        max_vol = 0
        while i < j:
            h = min(heights[i], heights[j])
            max_vol = max((j-i)*h, max_vol)
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        
        return max_vol