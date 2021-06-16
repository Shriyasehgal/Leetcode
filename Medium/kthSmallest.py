'''Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.'''

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        matrix_1=[]
        for i in range(0,len(matrix[0])):
            matrix_1.extend(matrix[i])
        matrix_1.sort()
        return matrix_1[k-1]
