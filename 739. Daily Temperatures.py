class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = temperatures
        n = len(temps)
        answer = [0] * n
        stk = []
        for i, t in enumerate(temps):
            while stk and stk[-1][0] < t:
