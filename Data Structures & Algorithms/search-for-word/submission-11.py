class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        seen = set()
        def dfs(i, j, index):
            if index == len(word):
                return True
            if (i < 0 or i >= len(board) or j < 0 or j >= len(board[i])):
                return False
            if (i,j) in seen:
                return False
            if word[index] != board[i][j]:
                return False
            
            seen.add((i,j))
            # print(f"move to ({i},{j})")
            
            for dir in directions:
                if (dfs(i + dir[0], j + dir[1], index + 1)):
                    return True
            seen.remove((i,j))
            
            return False
            


        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    # print(f"start at ({i},{j})")
                    if dfs(i, j, 0):
                        return True
                    
        return False


    