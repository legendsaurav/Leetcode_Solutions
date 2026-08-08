class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_len = 0

        def dfs(node, go_left, current_length):
            if not node:
                return
            
            # Track the maximum path length seen so far
            self.max_len = max(self.max_len, current_length)
            
            if go_left:
                dfs(node.left, False, current_length + 1)
                dfs(node.right, True, 1)
            else:
                dfs(node.right, True, current_length + 1)
                dfs(node.left, False, 1)

        # Explore both starting directions from the root node
        dfs(root, True, 0)
        dfs(root, False, 0)
        
        return self.max_len
