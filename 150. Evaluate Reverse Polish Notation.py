class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        hashset = {"+","-","*","/"}
        stk = []
        for i in tokens:
            if i not in hashset:
                stk.append(int(i))
            else:
