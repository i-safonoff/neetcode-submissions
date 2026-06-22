class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()
        for s in strs:
            sorted_s = str(sorted(s))
            if sorted_s not in groups.keys():
                groups[sorted_s] = []
            groups[sorted_s].append(s)

        return list(groups.values())