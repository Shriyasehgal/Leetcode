class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s)!=len(pattern): return False
        patternDict = {}
        values = set()
        for i in range(len(pattern)):
            if pattern[i] in patternDict:
                if patternDict[pattern[i]] != s[i]: return False
            elif s[i] in values: return False
            else:
                patternDict[pattern[i]] = s[i]
                values.add(s[i])
        return True