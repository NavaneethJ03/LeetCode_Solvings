class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1
        while l<=r:
            m = (r + l)//2
            if nums[m] == target:
                return m
            else:
                if target < nums[m]:
                    r = m-1 
                else:
                    l = m + 1
        if target > nums[m]:
            return m+1
        else:
            return m

# Time Complexity - O(logn)
# Space Complexity - O(1)



