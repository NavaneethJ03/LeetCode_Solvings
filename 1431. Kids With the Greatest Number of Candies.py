class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxx =  max(candies)
        result = []
        for i in range(0,len(candies)):
            candies[i] += extraCandies
            if candies[i] >= maxx:
                result.append(True)
            else:
                result.append(False)
        return result
# Time Complexity - O(n)
# Space Complexity - O(n)

