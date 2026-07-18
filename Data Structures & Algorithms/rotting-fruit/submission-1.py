class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = deque()
        finalDepth = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j,0))

        while queue:
            i, j, depth = queue.popleft()

            # explore edges
            if i + 1 < len(grid) and grid[i+1][j] == 1:
                grid[i+1][j] = 2
                queue.append((i+1,j,depth + 1))
            if i - 1 > -1 and grid[i-1][j] == 1:
                grid[i-1][j] = 2
                queue.append((i-1,j,depth + 1))
            if j + 1 < len(grid[i]) and grid[i][j+1] == 1:
                grid[i][j+1] = 2
                queue.append((i,j+1,depth + 1))
            if j - 1 > -1 and grid[i][j-1] == 1:
                grid[i][j-1] = 2
                queue.append((i,j-1,depth + 1))

            finalDepth = max(depth, finalDepth)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        
        return finalDepth
