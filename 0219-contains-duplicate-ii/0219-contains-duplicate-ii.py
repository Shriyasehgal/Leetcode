class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dictt = defaultdict(list)
        for i,n in enumerate(nums):
            if n in dictt and i - dictt[n][-1] <= k:
                return True
            dictt[n].append(i)
        return False
            