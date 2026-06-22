class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = dict()
        for i in range(len(nums)):
            if counter.get(target - nums[i], None) is not None:
                return [counter[target - nums[i]], i]
            else:
                counter[nums[i]] = i