class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        i = 0
        j = len(tokens)-1
        max_score = 0
        score = 0
        while i <= j:
            if tokens[i] <= power:
                score+=1
                power-=tokens[i]
                i+=1
                max_score = max(score,max_score)
            elif score >0 :
                score-=1
                power+=tokens[j]
                j-=1
            else:
                break
        return max_score
                
            