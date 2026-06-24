class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        cur_max = 0
        stack = []

        heights.append(0) 
        
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][0] > heights[i]:
                h, j = stack.pop()
                cur_max = max(cur_max, h * (i - j))
                start = j
            
            stack.append((heights[i], start))
        
        return cur_max