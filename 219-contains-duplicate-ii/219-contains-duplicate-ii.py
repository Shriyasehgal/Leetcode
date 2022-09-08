from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_dict = defaultdict(lambda: None)
        for i,num in enumerate(nums):
            if nums_dict[num] !=None and abs(nums_dict[num] - i) <=k:
                return True
            nums_dict[num] = i
        return False
                
            
            
        