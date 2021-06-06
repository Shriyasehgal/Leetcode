"""Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets."""


from collections import Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        nums, triplets = list(counter.keys()), set()
        if counter[0] >= 3:
            triplets.add((0, 0, 0))
        positives, negatives = [n for n in nums if n > 0], [n for n in nums if n < 0]
        for a in negatives:
            for b in positives:
                c = -(a + b)
                if c in counter and ((c != a and c != b) or counter[c] > 1):
                    triplets.add(tuple(sorted([a, b, c])))
        return triplets
