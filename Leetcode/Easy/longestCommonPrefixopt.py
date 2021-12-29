'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        s = ''
        for x in list(zip(*strs)):
            if x.count(x[0]) == len(x):
                s+= x[0]
            else:
                break
        return s
