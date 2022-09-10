class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        res = False
        visited = set()
        def helper(i):
            nonlocal res
            if i in visited:
                return
            visited.add(i)
            if i >= len(arr) or i <0:
                return
            if arr[i] == 0:
                res = True
                return
            helper(i+arr[i])
            helper(i-arr[i])
        helper(start)
        return res