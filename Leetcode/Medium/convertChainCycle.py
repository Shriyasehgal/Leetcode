'''The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);'''


from itertools import cycle,chain
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s)<=numRows or numRows==1: return s
        i=0
        res=[[] for _ in range(numRows)]
        for j in cycle(chain(range(0,numRows),range(numRows-2,0,-1))):
            if i == len(s):
                break
            res[j].append(s[i])
            i+=1

        res=["".join(x) for x in res]
        res="".join(res)
        return res
