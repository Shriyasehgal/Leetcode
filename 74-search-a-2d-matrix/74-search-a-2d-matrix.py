class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Taking O(m) time
        for i in range(len(matrix)):
            if matrix[i][0] > target:
                return False
            if matrix[i][0] <= target and matrix[i][-1] >=target:
                break
        #Taking log(n) time
        l = 0
        r = len(matrix[0]) - 1
        while l <= r:
            m = int((l+r)/2)
            if matrix[i][m] == target:
                return True
            elif matrix[i][m] > target:
                r = m-1
            else:
                l = m+1
        return False