class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque([(nums[0],0)])
         
        i = 1
        res = []
        while i <= len(nums):
            if i >= k:
                res.append(q[0][0])
            if i== len(nums): break
            while q and i - q[0][1] >= k:
                q.popleft()
            while q and q[-1][0] < nums[i]:
                q.pop()
            q.append((nums[i],i))
            i+=1
        return res
                
        
                
        