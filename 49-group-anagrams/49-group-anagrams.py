from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictAnagram = defaultdict(list)
        for s in strs:
            count = [0]*26 #a-z
            for i in s:
                count[ord(i)-ord('a')] +=1
            dictAnagram[tuple(count)].append(s)
        return dictAnagram.values()
        