class Solution:
    def findPivot(self,nums):
        el = nums[-1]
        l = 0
        r = len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m] > el:
                l = m+1
            else:
                r = m-1
        return l

    def binarySearch(self,nums,target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m 
            elif nums[m] < target:
                l = m+1
            else:
                r = m-1
        return -1
        
    def search(self, nums: List[int], target: int) -> int:
        l = self.findPivot(nums)
        if l == 0:
            return self.binarySearch(nums,target)
        
        val = self.binarySearch(nums[0:l],target)
        if val!=-1:
            return val
        val = self.binarySearch(nums[l:], target)
        if val!=-1:
            return l+ val
        return -1

            
        