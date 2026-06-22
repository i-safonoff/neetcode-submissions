class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for st in strs:
            res += f"{len(st)},"
        res += "#"
        res += ''.join(strs)
        return res

    def decode(self, s: str) -> List[str]:

        delimiter_index = s.index('#')
        lens = s[:delimiter_index]
        sts = s[delimiter_index + 1:]
        
        result = []
        i = 0
        for l in lens.split(','):
            if l == "":
                continue
            le = int(l)
            result.append(sts[i:i+le])
            i += le

        return result