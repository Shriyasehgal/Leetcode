class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l < r:
            m = (l+r)//2
            # m to p is not sorted
            if nums[m-1]>nums[m]:
                return nums[m]
            else:
                if nums[m] > nums[r]:
                    l = m+1
                #m to p is sorted
                else:
                    if nums[m] < nums[r]:
                        r = m-1
                    else:
                        r = r-1
        return nums[l]