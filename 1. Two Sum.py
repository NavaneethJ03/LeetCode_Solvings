class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        i = 0 
        output=[]
        while i < n :
            for j in nums:
                if (nums[i] + j = target ):
