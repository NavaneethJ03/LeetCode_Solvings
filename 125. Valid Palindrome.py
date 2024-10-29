class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_dup=''
        for i in s.lower():
            if i.isalnum():
                s_dup=s_dup+i
        if s_dup==s_dup[::-1]:
            return True
        return False
# Brute force method 
