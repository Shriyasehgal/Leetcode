'''Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.



Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]'''


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(l,r):
            seen = set()
            if l == r:
                all_res.append(nums[:])
            else:
                for i in range(l,r):

                    if nums[i] in seen: continue
                    nums[i],nums[l]=nums[l],nums[i]
                    backtrack(l+1,r)
                    nums[l],nums[i]=nums[i],nums[l]
                    seen.add(nums[i])


        all_res=[]
        backtrack(0,len(nums))
        return all_res
