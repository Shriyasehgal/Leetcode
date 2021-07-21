'''The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);'''
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s)<=numRows or numRows==1: return s

        res=[[] for _ in range(numRows)]
        j=0
        i=0
        n=len(s)-1

        while i <= n:
            while i<=n and j<len(res)-1:
                res[j].append(s[i])
                j+=1
                i+=1

            while i<=n and j>0:
                res[j].append(s[i])
                j-=1
                i+=1
        res=["".join(x) for x in res]
        res="".join(res)
        return res
