class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ''
        for prefix in zip(*strs):
            if len(set(prefix))!=1: break
            s+=prefix[0]
        return s