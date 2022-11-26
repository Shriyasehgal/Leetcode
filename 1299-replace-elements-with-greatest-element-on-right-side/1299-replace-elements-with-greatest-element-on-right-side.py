class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1]*len(arr)
        maxx = res[-1]
        for i in range(len(arr)-1,-1,-1):
            res[i] = maxx
            if arr[i] > maxx:
                maxx = arr[i]
            
        return res
        