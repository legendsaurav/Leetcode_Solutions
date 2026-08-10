# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        memo={}
        def solve(n):
            if n in memo :
                return memo[n]
            if n%2 ==0:
                return[]
            if n ==1:
                return[TreeNode(0)]
            result=[]
            for left in range (1,n,2):
                right =n-1-left
                left_tree=solve(left)
                right_tree=solve(right)
                for l in left_tree:
                    for r in right_tree:
                        root=TreeNode(0)
                        root.left=l
                        root.right=r
                        result.append(root)
            memo[n]=result
            return result
        return solve(n)