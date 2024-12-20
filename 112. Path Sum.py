class Solution:
  def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    def has_sum(root,curr_sum):
      if not root:
        return False 
      curr_sum += root.val
      if not root.right and not root.left:
        return root.val == targetSum
      return has_sum(root.right,curr_sum) or has_sum(root.left, curr_sum)
    return has_sum(root,0)

# Time Complexity - O(n) , n  - no of nodes in tree 
# Space Complexity - O(h) , h - height of tree 
