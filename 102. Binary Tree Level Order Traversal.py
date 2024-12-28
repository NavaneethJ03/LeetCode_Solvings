class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return ans
        
        queue = deque()
        queue.append(root)
        
        
        while queue:
            level = []
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                level.append(node.val)

                if node.left: queue.append(node.left)                
                if node.right: queue.append(node.right)
            
            ans.append(level)

        return ans

# Time Complexity: O(n)
# Space Complexity: O(n)
