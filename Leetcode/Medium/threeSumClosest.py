'''Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.



Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).'''
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        minn=float('inf')
        minn_sum=0
        for i in range(len(nums)-2):
            l, r = i + 1, len(nums) - 1
            while l < r :
                s = nums[i] + nums[l] + nums[r]
                curr_diff = abs(target - s)
                if curr_diff == 0:
                    return s
                elif curr_diff < minn :
                    minn = curr_diff
                    minn_sum = s
                if s < target: l += 1
                elif s > target: r -= 1
        return minn_sum

s=Solution()
s.threeSumClosest([-1,2,1,-4],1)
