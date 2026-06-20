from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_heap = []
        num_count = dict(Counter(nums))
        gen = ((v, k) for k, v in num_count.items())
        for t in gen:
            heapq.heappush(num_heap, t)
            if len(num_heap) > k:
                heapq.heappop(num_heap)

        return [v for k, v in num_heap]
