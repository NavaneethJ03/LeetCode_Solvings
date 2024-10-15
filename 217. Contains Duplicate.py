class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) < len(nums):
            return True

        else:
            return False

# Time Complexity O(n)

# Another Solution

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            if num in s:
                return True
            else:
                s.add(num)
        return False
# Time Complexity o(n)

# Both are one of the optimal solutions 

# Hipppp hippp hurrrah hhh 
