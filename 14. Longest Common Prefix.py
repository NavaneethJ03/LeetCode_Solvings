class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = float("inf")
        for s in strs:
            if len(s) < min_len:
                min_len = len(s)
