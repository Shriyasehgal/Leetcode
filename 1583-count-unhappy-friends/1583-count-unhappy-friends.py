class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        rank = [[-1 for i in range(n)] for j in range(n)]
        for i,p in enumerate(preferences):
            count = 0
            for j in range(len(p)):
                rank[i][p[j]] = count
                count+=1
        graph = defaultdict(list)
        
        for pair in pairs:
            (a,b) = pair
            graph[a] = b
            graph[b] = a
        res = 0
        for item in graph:
            for p in preferences[item]:
                if p == graph[item]:
                    break
                #Now we knoe that item prefers p over its pair.
                #Checking if p prefers item over p's pair
                idxOfItem = rank[p][item] #Preferences for p
                idxOfPair = rank[p][graph[p]]
                
                if idxOfItem < idxOfPair:
                    res+=1
                    break
        return res
                
            
            
            
        
            