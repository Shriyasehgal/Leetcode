'''Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:'''


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res=[]
        if numRows>=1:

            res.append([1])
        if numRows>=2:
            res.append([1,1])

        for i in range(2,numRows):
            curr_row=[1]
            for j in range(1,len(res[i-1])):
                curr_row.append(res[i-1][j-1]+res[i-1][j])
            curr_row.append(1)
            res.append(curr_row)

        return res
