class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        collection = dict()
        seen = set()
        max_len = 0
        for num in nums:
            if num in seen:
                continue
            if (num - 1 not in collection.keys()) and (num + 1 not in collection.keys()):
                # Создать new цепочку
                collection[num] = (1, num)
                max_len = max(max_len, 1)
            elif num - 1 in collection.keys() and num + 1 not in collection.keys():
                # Достроить справа
                l, start = collection[num-1]
                collection[num] = (l + 1, start)
                collection[start] = (l + 1, start)
                max_len = max(max_len, l + 1)
            elif num - 1 not in collection.keys() and num + 1 in collection.keys():
                # Достроить слева
                l, start = collection[num+1]
                collection[num] = (l + 1, num)
                collection[start + l - 1] = (l + 1, num)
                max_len = max(max_len, l + 1)
            else:
                # Склеить цепочки
                left_l, left_start = collection[num-1]
                right_l, right_start = collection[num+1]
                collection[left_start] = (left_l + 1 + right_l, left_start)
                collection[right_start + right_l - 1] = (left_l + 1 + right_l, left_start)
                max_len = max(max_len, left_l + 1 + right_l)
            seen.add(num)
        return max_len