'''A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.'''




class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count1 = 0
        count2=0
        
        if int(s[0])==0:
            return 0
        
        if len(s)==1:
            return 1
            
        if len(s)==2:
            if 11<=int(s)<=26 and int(s) not in [10,20]:
                return 2
            elif 1<=int(s)<=9:
                return 0
            elif int(s) in [10,20]:
                return 1
        
        
        count1 = self.numDecodings(s[1:])
               
            
        if 10<=int(s[:2])<=26:
            count2 = self.numDecodings(s[2:])
            
        elif 1<=int(s[:2])<=9:
            count2= 0
        
            
        
        return count1+count2
      
            

