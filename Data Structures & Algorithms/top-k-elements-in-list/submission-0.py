class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict()
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        
        return sorted(counter.keys(), key=lambda x: -counter[x])[:k]