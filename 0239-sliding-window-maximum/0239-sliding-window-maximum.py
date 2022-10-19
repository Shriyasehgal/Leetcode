class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = []
        for i in range(k):
            heappush(window,(-nums[i],i))
        res.append(-window[0][0])
        start = 1
        end = k
        while end < len(nums):
            while window and window[0][1]<start:
                heappop(window)
            heappush(window,(-nums[end],end))
            res.append(-window[0][0])
            start+=1
            end+=1
        return res
        
                
        