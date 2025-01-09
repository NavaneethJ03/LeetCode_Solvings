class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n = len(pref)
        ans = 0
        for i in words:
            ref = i[:n]
            if pref == ref:
                ans += 1 

        return ans

# Time Complexity - O(n)
# Space Complexity - O(1)
