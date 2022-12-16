class Solution:
    def climbStairs(self, n: int) -> int:
        his = []
        for i in range(n+1):
            if i<=2:
                his.append(i)
            elif i>2:
                print(his)
                his.append(his[i-2] + his[i-1])
        return his[-1]
