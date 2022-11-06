class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        brickMap = defaultdict(lambda : len(wall))
        for wallIdx in wall:
            summIdx = 0
            for i in range(len(wallIdx)-1):
                summIdx+=wallIdx[i]
                brickMap[summIdx]-=1
        if not brickMap: return len(wall)
        return min(list(brickMap.values()))
        
                
                
            
        