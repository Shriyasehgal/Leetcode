'''Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].



Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1'''


class Solution(object):
    def binarySearch(self,arr,s,l,num):

        while True:
            if s>=l and arr[s]!=num:
                if arr[s]>num:
                    return s
                else:
                    return s+1
            mid=(s+l)//2
            if arr[mid]==num: return None
            if arr[mid] >= num: l=mid-1
            else: s=mid+1

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=[nums[0]]
        for i in range(1,len(nums)):
            if nums[i]>res[-1]:
                res.append(nums[i])
            else:
                replace=self.binarySearch(res,0,len(res)-1,nums[i])
                if replace==None:
                    continue
                else:
                    res[replace]=nums[i]
        return len(res)
s=Solution()
s.lengthOfLIS([3,5,6,2,5,4,19,5,6,7,12])
