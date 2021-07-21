'''You are given an array of strings words (0-indexed).

In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move any character from words[i] to any position in words[j].

Return true if you can make every string in words equal using any number of operations, and false otherwise.'''

class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        sum_elements="".join(words)
        if len(sum_elements) % (len(words)) != 0:
            return False
        
        dic_equal={}
        for el in sum_elements:
            if el not in dic_equal:
                dic_equal[el]=1
            else:
                dic_equal[el]+=1
        
        for i in dic_equal.values():
            if i% (len(words))!=0:
                return False
            
        return True
