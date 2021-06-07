class Solution(object):
    def longestCommonPrefix(self, strs):
        s = ''
        for x in list(zip(*strs)):
            if x.count(x[0]) == len(x):
                s+= x[0]
            else:
                break
        return s
