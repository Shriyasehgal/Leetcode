'''Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]'''
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(l,r):
            if l == r:
                all_res.append(nums[:])
            else:
                for i in range(l,r):
                    nums[i],nums[l]=nums[l],nums[i]
                    backtrack(l+1,r)
                    nums[l],nums[i]=nums[i],nums[l]


        all_res=[]
        backtrack(0,len(nums))
        return all_res



        all_res=[]
        backtrack(nums,[])
        return all_res
