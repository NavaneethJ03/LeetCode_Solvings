class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        for ops in operations:
            if ops == "+":
                stk.append(int(stk[-1]) + int(stk[-2]))
