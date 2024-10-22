class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums1 = []
        for i in nums:
            nums1.append(i*i)
        nums1.sort()
        return nums1
        
