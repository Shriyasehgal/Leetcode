'''Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
'''
class Solution:
    def generateParenthesis(self, n) :
        s9={"()"}
        y=2
        while(y<=n):
            s8=s9
            s9=set()
            for i in s8:
                for j in range(len(i)):
                    s3=i[:j]+'()'+i[j:]
                    s9.add(s3)
            y=y+1
        return list(s9)


s=Solution()
s.generateParenthesis(8)
