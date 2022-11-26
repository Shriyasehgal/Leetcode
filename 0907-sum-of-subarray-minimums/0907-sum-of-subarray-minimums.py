class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        arr = [0] + arr
        stack = [0]
        res = [0]*len(arr)
        for j in range(1, len(arr)):
            while arr[stack[-1]] > arr[j]:
                stack.pop()
            i = stack[-1]
            res[j] = res[i] + (j-i)*arr[j]
            stack.append(j)
        return sum(res)%mod