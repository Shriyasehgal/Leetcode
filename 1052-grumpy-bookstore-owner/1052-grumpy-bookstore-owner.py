class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        i = 0
        j = 0
        curr = sum([customers[i] for i in range(len(grumpy)) if grumpy[i]==0])
        ans = curr
        while j < len(grumpy): 
            if grumpy[j] == 1:
                curr+=customers[j]
            while j-i+1 > minutes:
                if grumpy[i] == 1:
                    curr -= customers[i]
                i+=1
            ans = max(ans,curr)
            j+=1
        return ans
                
            