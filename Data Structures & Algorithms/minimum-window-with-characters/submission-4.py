from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        l = 0
        need = Counter(t)
        requiered = len(need)
        have = 0

        window = {}
        l_res, r_res = -1, -1

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1

            if s[r] in need and window[s[r]] == need[s[r]]:
                have += 1


            while have == requiered: #all(window.get(c, 0) >= need[c] for c in need):
                if (r_res == -1 and l_res == -1) or r - l + 1 < r_res - l_res + 1:
                    l_res, r_res = l, r
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l += 1
        
        return s[l_res:r_res+1]