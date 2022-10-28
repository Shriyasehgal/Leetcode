class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt = defaultdict(list)
        for i in range(len(strs)):
            c = [0]*26
            for j in range(len(strs[i])):
                c[ord(strs[i][j]) - ord('a')]+=1
            dictt[tuple(c)].append(strs[i])
        return  dictt.values()
                