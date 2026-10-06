import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = []

        res = []
        l, r = 0, k - 1
        for i in range(k):
            heapq.heappush_max(h, (nums[i], i))

        res = [h[0][0]]

        while r < len(nums) - 1:
            l += 1
            r += 1

            heapq.heappush_max(h, (nums[r], r))
          
            while h and h[0][1] < l:
                heapq.heappop_max(h)
            
            m, i = h[0]
            if l <= i <= r:
                res.append(m)
        
        return res

            