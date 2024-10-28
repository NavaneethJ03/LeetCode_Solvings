class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1 
        
        while l <= r:
            m  = l + ((r - l)//2)
            if target == nums[m]:
                return m 
            else:
                if target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        return -1


        
