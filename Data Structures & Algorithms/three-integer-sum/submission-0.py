class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        result = set()
        for i in range(len(nums)):
            target = -nums[i]
            l, r = i + 1, n - 1

            while l < r:
                cur_sum = nums[l] + nums[r]
                if cur_sum == target:
                    result.add((nums[i], min(nums[l], nums[r]), max(nums[l], nums[r])))
                    l += 1
                    r -= 1
                elif cur_sum < target:
                    l += 1
                else:
                    r -= 1
        return [list(item) for item in result]