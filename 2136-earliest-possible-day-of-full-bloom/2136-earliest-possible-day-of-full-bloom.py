class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        totalPlantTime = 0
        lastGrowTime = 0
        for growtime, planttime in sorted(zip(growTime, plantTime), reverse=True):
            totalPlantTime += planttime
            lastGrowTime = max(totalPlantTime+growtime, lastGrowTime)
        return lastGrowTime