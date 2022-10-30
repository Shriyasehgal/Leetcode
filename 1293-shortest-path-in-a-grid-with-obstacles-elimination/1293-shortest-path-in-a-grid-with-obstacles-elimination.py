class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid), len(grid[0])
        q = deque([(0,0,0)]) # i,j,r where r = no. of obstacles removed till now
        q2 = deque([])
        step = 0
        visited = set((0,0,0))
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        if k >= len(grid) + len(grid[0]) - 2: return len(grid) + len(grid[0]) - 2
        while q:
            i,j,r = q.pop()
            if i == len(grid)-1 and j == len(grid[0])-1: return step
            for a, b in directions:
                nr, nc = i + a, j + b
                if 0 <= nr < m and 0 <= nc < n: #isValid
                    new_state = (nr, nc, r + grid[nr][nc])
                    if new_state[2] <= k and new_state not in visited:
                        visited.add(new_state)
                        q2.append(new_state)
            if not q:
                q,q2 = q2,q
                step+=1
                
        return -1
            
        
        