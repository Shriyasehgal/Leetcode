'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        
        dict={'(':')','[':']','{':'}'}   
        stack=[]
        
        
        
        for i in range(0,len(s)):
            if s[i] in dict.keys():
                stack.append(s[i])
            elif len(stack)==0:
                return False
            elif stack[-1] in dict.keys() and dict[stack[-1]]==s[i]:
                stack.pop()
            else:
                return False
            
            
        if len(stack)==0:
            return True  
            
        return False
            
            
