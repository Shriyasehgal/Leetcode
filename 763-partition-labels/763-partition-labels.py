class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        c = Counter(s)
        sett = set()
        res = []
        curr = 0
        for char in s:
            c[char]-=1
            sett.add(char)
            curr+=1
            if c[char] == 0:
                sett.remove(char)
                if not sett:
                    res.append(curr)
                    curr = 0
        return res
                    