class Solution:
    def isValid(self, s: str) -> bool:
        if s == "": return True

        mapping = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        stack = []
        for sym in s:
            if sym in mapping:
                stack.append(sym)
            else:
                if stack:
                    last = stack.pop()
                    if sym != mapping[last]:
                        return False
                else:
                    return False
        if stack: return False
        return True