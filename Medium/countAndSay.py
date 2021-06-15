'''The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character. Then for each group, say the number of characters, then say the character. To convert the saying into a digit string, replace the counts with a number and concatenate every saying.

For example, the saying and conversion for digit string "3322251":


Given a positive integer n, return the nth term of the count-and-say sequence.'''

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return '1'
        temp_res='11'
        for i in range(3,n+1):
            s=0
            l=1
            temp=''
            for j in range(0,len(temp_res)):
                if l == len(temp_res):
                    temp=temp+ str(len(temp_res[s:l]))+temp_res[s]
                elif temp_res[s]==temp_res[l]:
                    l+=1
               
                else:
                    temp=temp+ str(len(temp_res[s:l]))+temp_res[s]
                    s=l
                    l+=1
            temp_res=temp
                    
        return temp_res
