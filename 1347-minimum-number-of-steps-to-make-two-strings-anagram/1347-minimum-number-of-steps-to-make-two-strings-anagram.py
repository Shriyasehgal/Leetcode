class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dictt = defaultdict(lambda : 0)
        for i in range(len(s)):
            dictt[s[i]]+=1
            dictt[t[i]]-=1
        return sum([abs(i) for i in dictt.values()])//2
            
        