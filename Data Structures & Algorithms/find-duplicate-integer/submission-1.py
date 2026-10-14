class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while slow != fast or (slow == 0 and fast == 0):
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        new_slow = 0
        while new_slow != slow:
            slow = nums[slow]
            new_slow = nums[new_slow]
        return new_slow