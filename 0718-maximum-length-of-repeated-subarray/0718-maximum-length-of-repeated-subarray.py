class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        maxx = 0
        dp = [[0 for i in range(len(nums2)+1)] for j in range(len(nums1)+1)]
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] =1 + dp[i-1][j-1]
                    maxx = max(maxx,dp[i][j])
        return maxx
                
        