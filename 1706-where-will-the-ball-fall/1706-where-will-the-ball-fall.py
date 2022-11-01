class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        result = []
        X, Y = len(grid[0]), len(grid)
        # go through all start point (x, y)
        for x in range(len(grid[0])):
            y = 0
            # setting the searching boundary 
            while 0 <= x < X and 0 <= y < Y:
                # break condition
                # 1. hit the boundary
                # 2. the neighbor is the opposite direction
                direction = grid[y][x]
                neighbor = grid[y][x+direction] if 0 <= x+direction < X else -direction
                if direction != neighbor:
                    break
                # iterate condition
                x, y = x+direction, y+1
            result.append(-1 if y != Y else x)
        return result