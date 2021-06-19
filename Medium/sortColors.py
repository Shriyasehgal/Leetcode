'''Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 '''


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=-1
        j=len(nums)
        l=0
        while l<j:
            if nums[l]==0:
                nums.insert(0,nums.pop(l))
                i+=1

            elif nums[l]==2:
                nums.append(nums.pop(l))
                j-=1
                l-=1

            l+=1
        return nums
