class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]
        max_len = 0
        for a in arr:
            a_set = set(a)
            if len(a) != len(a_set):
                continue
            for b in dp:
                if not a_set & b:
                    dp.append(a_set|b)
                    max_len = max(max_len,len(a_set)+len(b))
        return max_len
                