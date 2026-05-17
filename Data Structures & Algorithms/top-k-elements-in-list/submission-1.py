class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Non-naive solution using bucket sort

        counts = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            counts[n] = 1 + counts.get(n, 0)
        for n, c in counts.items():
            freq[c].append(n)
        
        ans = []
        for i in range(len(freq) - 1, 0, -1):
            for v in freq[i]:
                ans.append(v)
                if len(ans) == k:
                    return ans
