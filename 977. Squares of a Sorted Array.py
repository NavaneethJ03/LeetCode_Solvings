class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums1 = []
        for i in nums:
            nums1.append(i*i)
        nums1.sort()
        return nums1

# Time Complexity -  O(n logn)

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        pos = n - 1
        
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[pos] = nums[left] ** 2
                left += 1
            else:
                result[pos] = nums[right] ** 2
                right -= 1
            pos -= 1
        
        return result

 
        
