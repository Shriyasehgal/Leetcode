class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        el = nums[-1]
        l = 0
        r = len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m] > el:
                l = m+1
            else:
                r = m-1
        return nums[l]
