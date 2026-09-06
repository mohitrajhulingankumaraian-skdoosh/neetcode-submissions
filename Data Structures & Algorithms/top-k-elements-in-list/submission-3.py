class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq
        num_count = dict(Counter(nums))
        freq_heap = []
        for (key,v) in num_count.items():
            heapq.heappush(freq_heap, (v,key))
            #print(len(freq_heap))
            if len(freq_heap) > k:
                heapq.heappop(freq_heap)
                #print(freq_heap)
        
        
        
        return [n for _,n in freq_heap]

        