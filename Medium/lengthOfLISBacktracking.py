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
    def __init__(self):
        self.max_count=0
        self.dictLIS={}

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.helper(nums,[],0,0)
        return self.max_count


    def helper(self, nums,subset,curr,count):
        if curr in self.dictLIS.keys(): return self.dictLIS[curr]
        if len(subset)>=2 and subset[-1]<=subset[-2]: return
        else: self.dictLIS[curr]=count
        if curr>=len(nums):
            if self.max_count<count:
                self.max_count=count
            return


        subset.append(nums[curr])
        count+=1
        self.helper(nums,subset,curr+1,count)
        subset.pop(-1)
        count-=1
        self.helper(nums,subset,curr+1,count)


s=Solution()
s.lengthOfLIS([10,9,2,5,3,7,101,18])
