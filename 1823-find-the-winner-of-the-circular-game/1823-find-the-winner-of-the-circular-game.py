class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        inc = k-1 #number of increaments
        nums = [i+1 for i in range(n)]
        i = 0
        while len(nums)!=1:
            k = inc%len(nums)
            if i+k < len(nums):
                i = i+k
            else:
                i = k - (len(nums) - i)
            nums.pop(i)
            if i >= len(nums): i=0
        return nums[0]