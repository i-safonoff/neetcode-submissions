class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, j = 0, 0
        res = 0
        counts = {}
        while j < len(s):
            counts[s[j]] = counts.get(s[j], 0) + 1
            max_freq = max(counts.values())
            while j - i + 1 - max_freq > k:
                counts[s[i]] -= 1
                i += 1
                max_freq = max(counts.values())
            res = max(res, j - i + 1)
            j += 1
        return res