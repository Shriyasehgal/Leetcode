class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        subset = set()
        res = 0
        while j < len(s):
            
            while s[j] in subset:
                subset.remove(s[i])
                i+=1
            subset.add(s[j])
            res = max(res,j-i+1)
            j+=1
        return res
                