# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans=float("-inf")
        def dfs(node):
            nonlocal ans 
            if node is None :
                return 0
            left =max(0,dfs(node.left))
            right =max(0,dfs(node.right))
            current=node.val+left+right
            ans=max(ans,current)
            return node.val+max(left,right)
        dfs(root)
        return ans