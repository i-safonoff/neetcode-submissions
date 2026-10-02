class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subs = ""
        res = 0
        for sym in s:
           if sym not in subs:
               subs += sym
               res = max(res, len(subs))
           else:
                while sym in subs:
                    subs = subs[1:]
                subs += sym
        return res
    