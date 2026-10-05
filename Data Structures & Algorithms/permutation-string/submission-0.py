class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if len(s2) < k:
            return False

        l, r = 0, 0
        counter = {}
        for sym in s1:
            counter[sym] = counter.get(sym, 0) + 1
        cur = {}

        while r < len(s2):
            if s2[r] in s1:
                cur[s2[r]] = cur.get(s2[r], 0) + 1

            if r - l + 1 > k:
                if s2[l] in s1:
                    cur[s2[l]] = cur.get(s2[l], 1) - 1
                l += 1
            
            if cur == counter:
                return True

            r += 1
        return False
