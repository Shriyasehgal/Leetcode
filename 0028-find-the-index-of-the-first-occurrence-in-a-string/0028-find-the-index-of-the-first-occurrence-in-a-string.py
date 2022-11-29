class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack): return -1
        i = 0
        j = 0
        while j < len(haystack):
            while j < len(haystack) and j-i+1<len(needle):
                j+=1
            if haystack[i:j+1] == needle: return i
            i+=1
        return -1
        