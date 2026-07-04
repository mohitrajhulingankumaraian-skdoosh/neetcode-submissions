class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i, j = 1, max(piles)
        res = j
        while i <= j:
            k = (i + j)//2
            total_time = 0
            for p in piles:
                total_time += math.ceil(p / k)
            
            if total_time <= h:
                res = k
                j = k - 1
            else:
                i = k + 1
        
        return res