class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = [0,float('inf')] #[sum, abs(target - sum)]
        nums.sort()
        start = 0
        end = len(nums)-1
        while start < end:
            i = start + 1
            j = end - 1
            currentClosest = [0, float('inf')]
            while i <= j:
                mid = (i+j)//2
                summ = nums[start] + nums[mid] + nums[end]
                if summ == target:
                    return summ
                if abs(target - summ) < currentClosest[1]:
                    currentClosest = [summ , abs(target - summ)]
                if summ < target:
                    i = mid + 1
                else:
                    j = mid - 1
            if currentClosest[1] < ans[1]:
                ans = currentClosest
            if currentClosest[0] < target:
                start+=1
            else:
                end-=1
        return ans[0]
                
                    