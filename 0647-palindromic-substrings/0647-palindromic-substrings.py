class Solution:
    def countSubstrings(self, s: str) -> int:
        subStrings = 0
        #Calculting for the odd substrings
        for i in range(len(s)):
            l, r = i, i
            while l >=0 and r <= len(s)-1 and s[l] == s[r]:
                subStrings+=1
                l-=1
                r+=1
        #calculating for the even substrings
        for i in range(len(s)-1):
            l = i
            r = i+1
            while l>=0 and r <= len(s)-1 and s[l] == s[r]:
                subStrings+=1
                l-=1
                r+=1
        return subStrings