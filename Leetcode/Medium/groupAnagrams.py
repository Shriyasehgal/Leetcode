'''Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''
from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        strs_dict=defaultdict(list)
        strs_copy = strs[:]
        for i in range(len(strs)):
            strs[i]=''.join(sorted(strs[i]))
            strs_dict[strs[i]].append(strs_copy[i])

        return strs_dict.values()
