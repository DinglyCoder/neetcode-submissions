# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res = 0

        def dfs(node, depth):
            nonlocal res
            if node == None:
                return depth

            left = dfs(node.left, depth + 1)
            right = dfs(node.right, depth + 1)

            d = left - depth + right - depth - 2

            res = max(res, d)

            return max(left, right)

        dfs(root, 0)

        return res

