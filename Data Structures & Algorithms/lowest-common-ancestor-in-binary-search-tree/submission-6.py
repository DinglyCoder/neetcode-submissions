# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node, p, q):   
            if p.val == node.val or q.val == node.val:
                print("one")
                return node

            if p.val <= node.val and q.val <= node.val:
                print("left")
                return dfs(node.left, p, q)
            elif p.val >= node.val and q.val >= node.val:
                print("right")
                return dfs(node.right, p, q)

            print("diff")
            return node

        return dfs(root, p, q)       