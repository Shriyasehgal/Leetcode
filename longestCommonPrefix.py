class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        output=''
        if len(strs)==1:
            return strs[0]
        for j in range(0,min(map(len,strs))):
            for i in range(0,len(strs)-1):            
                if strs[i][j]!=strs[i+1][j]:
                    return output
            output=output+strs[i][j]
        return output
            
