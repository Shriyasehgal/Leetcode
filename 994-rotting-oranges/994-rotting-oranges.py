class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        prevQueue = deque([])
        newQueue = deque([])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    prevQueue.append((i,j))
            
        time = 0
        while prevQueue:
            roti,rotj = prevQueue.popleft()
            if roti > 0 and grid[roti-1][rotj] == 1:
                grid[roti-1][rotj] = 2
                newQueue.append((roti-1,rotj))
            if roti < rows-1  and grid[roti+1][rotj] == 1:
                grid[roti+1][rotj] = 2
                newQueue.append((roti+1,rotj))
            if rotj > 0 and grid[roti][rotj-1] == 1:
                grid[roti][rotj-1] = 2
                newQueue.append((roti,rotj-1))
            if rotj < cols-1 and grid[roti][rotj+1] == 1:
                grid[roti][rotj+1] = 2
                newQueue.append((roti,rotj+1))
            if not prevQueue and newQueue:
                time+=1
                prevQueue,newQueue = newQueue,prevQueue
                
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        return time