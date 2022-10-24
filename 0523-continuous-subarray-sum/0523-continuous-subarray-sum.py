class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem = {0:-1}
        summ = 0
        for i,n in enumerate(nums):
            summ+=n
            v = (summ) % k
            if v in rem and i - rem[v] > 1:
                return True
            elif v not in rem:
                rem[v] = i
        return False
                
            
        