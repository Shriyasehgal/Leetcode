from collections import Counter
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        s = Counter(words1)
        res = 0
        for key,val in Counter(words2).items():
            if val == 1 and s[key] == 1:
                res+=1
        return res
        