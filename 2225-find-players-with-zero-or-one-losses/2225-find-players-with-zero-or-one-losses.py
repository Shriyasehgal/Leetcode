class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        matchDict = defaultdict(lambda : 0)
        minPlayer, maxPlayer = float('inf'), -float('inf')
        for match in matches:
            matchDict[match[0]] += 0
            matchDict[match[1]] += 1
            minPlayer = min(minPlayer,match[0],match[1])
            maxPlayer = max(maxPlayer,match[0],match[1])
        answer = [[],[]]
        
        for i in range(minPlayer, maxPlayer+1):
            if i in matchDict:
                if matchDict[i] == 0: answer[0].append(i)
                elif matchDict[i] == 1: answer[1].append(i)
        return answer
                