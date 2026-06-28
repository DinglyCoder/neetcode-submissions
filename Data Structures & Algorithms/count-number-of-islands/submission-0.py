class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0

        def dfs(i, j):
            nonlocal grid
            if (grid[i][j] == "0"):
                return
            grid[i][j] = "0"

            print(grid)

            # stack = []
            
            if (i + 1 < len(grid) and grid[i + 1][j] == "1"):
                dfs(i+1, j)
            if (i > 0 and grid[i - 1][j] == "1"):
                dfs(i-1, j)
            if (j + 1 < len(grid[i]) and grid[i][j + 1] == "1"):
                dfs(i, j + 1)
            if (j > 0 and grid[i][j - 1] == "1"):
                dfs(i, j - 1)



            return

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        
        print("hello")

        return count