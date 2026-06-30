class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        def dfs(i, j, area):
            nonlocal grid
            if (grid[i][j] == 0):
                return
            grid[i][j] = 0

            # stack = []
            if (i + 1 < len(grid) and grid[i + 1][j] == 1):
                area = dfs(i+1, j, area + 1)
            if (i > 0 and grid[i - 1][j] == 1):
                area = dfs(i-1, j, area + 1)
            if (j + 1 < len(grid[i]) and grid[i][j + 1] == 1):
                area = dfs(i, j + 1, area + 1)
            if (j > 0 and grid[i][j - 1] == 1):
                area = dfs(i, j - 1, area + 1)

            return area

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    area = dfs(i, j, 1)
                    print(area)
                    maxArea = max(maxArea, area)
        
        print("bye")

        return maxArea