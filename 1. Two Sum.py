class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        i = 0 
        output=[]
        while i < n :
            for j in nums:
                if (nums[i] + j = target ):
                    output.append(i)
                    output.append(j)
                    else:
                        continue 
            i+=1

            return output
