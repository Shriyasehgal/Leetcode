class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        res=1
        i=1
        j=0
        while i<len(s):
            if s[i] in s[j:i]:             
                j= s[j:i].index(s[i])+j+1
           
            res= max(res, i-j+1)
            i+=1 
            
        return res
