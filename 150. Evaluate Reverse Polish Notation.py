class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        hashset = {"+","-","*","/"}
        stk = []
