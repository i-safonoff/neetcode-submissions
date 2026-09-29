class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        l, r = 0, len(height) - 1
        s = 0
        l_max, r_max = height[l], height[r]
        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(l_max, height[l])
                s += l_max - height[l]
            else:
                r -= 1
                r_max = max(r_max, height[r])
                s += r_max - height[r]
        return s








        # l, r = 0, len(height) - 1
        # left_max, right_max = 0, 0
        # s = 0
        # while l < r:
        #     if height[l] < height[r]:
        #         if height[l] >= left_max:
        #             left_max = height[l]
        #         else:
        #             s += left_max - height[l]
        #         l += 1
        #     else:
        #         if height[r] >= right_max:
        #             right_max = height[r]
        #         else:
        #             s += right_max - height[r]
        #         r -= 1
        # return s