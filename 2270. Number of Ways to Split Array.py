class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
      count = 0 
      leftsum = 0 
      rightsum =  sum(nums)
      for i in range(len(nums) - 1):
        leftsum += nums[i]
        rightsum -= nums[i] 
        if leftsum >= rightsum:
          count += 1 
      return count

# Time Complexity = O(n)
# Space Complexity - O(1)
