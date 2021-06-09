class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
      
        s=0
        l=len(nums)-1
        #if len(nums)<=2 and target not in nums: 
        while True:
            
            
            if s>=l and nums[s]!=target:
                if nums[s]>target:
                    return s
                else:
                    return s+1
            mid=int((l+s)/2)
            
            if target==nums[mid]:
                return mid
                
            if target<nums[mid]:
                l=mid-1
            
            else:
                s=mid+1
