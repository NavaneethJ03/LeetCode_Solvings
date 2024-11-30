class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0  # Edge case: empty array
        
        # Pointer to track the position of the next unique element
        i = 1  
        for j in range(1, len(nums)):
            if nums[j] != nums[j - 1]:  # Check if the current element is unique
                nums[i] = nums[j]      # Place it in the correct position
                i += 1  # Move the pointer for unique elements
        
        return i  # i represents the number of unique elements
