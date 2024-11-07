class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i = 0
        while(i < len(nums)):
            start =  i
             while (start < len(nums)-1) and (nums[i]+1 == nums[i+1]):
                i += 1
            if start != nums[i]:
