class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        diff = dict()
        for i in range(len(s)):
            diff[s[i]] = diff.get(s[i], 0) + 1
        for j in range(len(t)):
            diff[t[j]] = diff.get(t[j], 0) - 1
        
        for d in diff.values():
            if d != 0:
                return False
        return True