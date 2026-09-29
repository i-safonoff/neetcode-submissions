class Solution:
    def get_time_to_eat(self, piles, speed):
        s = 0
        for pile in piles:
            s += pile // speed
            if pile % speed: s += 1
        return s
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            m = (l + r) // 2
            t = self.get_time_to_eat(piles, m)
            if t > h:
                l = m + 1
            elif t <= h:
                r = m
        return l