class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapp = {'1':'','2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if not digits: return []
        res = ['']
        def helper(digits):
            nonlocal res
            if digits == '': return ''
            curr = []
            for c in mapp[digits[0]]:
                for j in res:
                    curr.append(j+c)
            res = curr
            helper(digits[1:])
        helper(digits)
        return res