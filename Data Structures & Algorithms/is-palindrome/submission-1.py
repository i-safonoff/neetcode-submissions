class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''
        for sym in s:
            if sym.isalnum():
                new_s += sym
        
        new_s = new_s.lower()
        l, r = 0, len(new_s) - 1
        while l < r:
            if new_s[l] != new_s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True