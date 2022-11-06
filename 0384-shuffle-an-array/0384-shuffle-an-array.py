class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums[:]
        self.nums = nums

    def reset(self) -> List[int]:
        
        return self.original

    def shuffle(self) -> List[int]:
        n = random.randint(0,len(self.nums)-1)
        val = self.nums.pop(n)
        self.nums.append(val)
        return self.nums
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()