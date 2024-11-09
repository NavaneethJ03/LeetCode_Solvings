class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_mul = 1 
        right_mul =  1 
        n =  len(nums)
        left_array = [0]*n
        right_array = [0]*n
        for i in range(n):
            j = -i -1 
            left_array[i] = left_mul
            right_array[j] = right_mul
            left_mul *= nums[i]
            right_mul *= nums[j]

        return [l*r for l, r in zip(left_array , right_array)]

# Time Complexity -  O(n)
# Space Complexity - O(n)
