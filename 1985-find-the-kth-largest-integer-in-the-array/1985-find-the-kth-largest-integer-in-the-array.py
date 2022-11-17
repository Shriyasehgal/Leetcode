class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [int(x) for x in nums]
        heapq.heapify(nums)
        ordered = []
        i = len(nums)
        while i >= k:
            elem = heapq.heappop(nums)
            ordered.append(elem)
            i-=1
        return str(ordered[-1])