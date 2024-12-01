class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        from math import gcd

        # Check if str1 and str2 share a common pattern
        if str1 + str2 != str2 + str1:
            return ""

        # Find the GCD of the lengths of str1 and str2
        gcd_len = gcd(len(str1), len(str2))

        # Return the substring of length gcd_len
        return str1[:gcd_len]
