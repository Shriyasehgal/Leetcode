class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = Counter(nums1)
        s = set(nums1)
        res = []
        for n in nums2:
            if n in s:
                c[n]-=1
                if c[n] >=0: res.append(n)
        return res