class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        unresolved = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            t = temperatures[i]
            if not unresolved:
                unresolved.append(i)
            else:
                while t > temperatures[unresolved[-1]]:
                    j = unresolved.pop()
                    result[j] = (i - j)
                    if not unresolved:
                        break
                unresolved.append(i)
        return result
