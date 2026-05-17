class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        
        counts = {}

        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
        
        sorted_nums = list(dict(sorted(counts.items(), key=lambda item: item[1], reverse=True)).keys())

        return sorted_nums[0:k]
        

        

        
