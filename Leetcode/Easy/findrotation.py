'''Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.'''


class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        if mat==target:
            return True
        for i in range(0,3):
            
            mat=zip(*mat)
            mat= [list(reversed(tup)) for tup in mat]
            if mat==target:
                return True
        return False
