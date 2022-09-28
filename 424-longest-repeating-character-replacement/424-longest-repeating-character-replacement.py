from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charDict = Counter()
        i = 0
        j = 0
        res = 1
        while j < len(s):
            #Checking if the window is valid
            charDict[s[j]]+=1
            charCount = charDict.most_common()[0][1]
            while (j-i+1) - charCount > k:
                charDict[s[i]] -=1
                i +=1
            
            res = max(res,j-i+1)
            j+=1
                
                
        return res
            
            