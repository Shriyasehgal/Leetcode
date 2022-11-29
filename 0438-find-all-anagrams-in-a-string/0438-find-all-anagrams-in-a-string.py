class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p): return []
        dict_p = {}
        dict_s = {}
        for i in range(len(p)):
            dict_p[p[i]] = 1 + dict_p.get(p[i],0)
            dict_s[s[i]] = 1 + dict_s.get(s[i],0)
        
        res = []
        if dict_p == dict_s: res.append(0)
        l = 0
        for i in range(len(p), len(s)):
            dict_s[s[i]] = 1 + dict_s.get(s[i],0)
            dict_s[s[l]] -= 1
            if dict_s[s[l]] == 0: del dict_s[s[l]]
            l+=1
            if dict_s == dict_p: res.append(l)
        return res