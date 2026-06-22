class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev = []
        post = []
        result = []
        for i in range(len(nums)):
            if not prev:
                prev.append(nums[i])
            else:
                prev.append(prev[i-1] * nums[i])
        for i in range(len(nums) - 1, -1, -1):
            if not post:
                post.append(nums[i])
            else:
                post.append(post[-1] * nums[i])

        result.append(post[-2])

        for i in range(1, len(nums) - 1):
            result.append(prev[i-1] * post[len(nums)-i - 2])

        result.append(prev[-2])

        return result