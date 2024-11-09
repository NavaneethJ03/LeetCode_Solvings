class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_mul = 1 
        right_mul =  1 
        n =  len(nums)
        left_array = [0]*n
