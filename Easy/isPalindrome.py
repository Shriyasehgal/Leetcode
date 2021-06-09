"""Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases."""

class Solution(object):
    def isPalindrome(self, m):
        """
        :type s: str
        :rtype: bool
        """
        s=[]
        stack=[]
        s.extend(i for i in m if i.isalnum())
        
        if len(s)==0:
            return True
       
    
        
        i=int((len(s)+1)/2)

        stack.extend(list(s[0:i]))
       
        if len(s)%2==1:
            stack.pop()
        
        while stack!=[] and s[i].lower()==stack[-1].lower():
            stack.pop()
            i+=1
            
            
        if len(stack)==0:
            return True
        return False
        
s=Solution()
s.isPalindrome("Marge, let's \"[went].\" I await {news} telegram.")
