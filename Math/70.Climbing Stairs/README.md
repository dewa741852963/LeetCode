###### tags: `Math`, `Dynamic Programming`, `Memoization`

# LeetCode 70.Climbing Stairs

You are climbing a staircase. It takes ```n``` steps to reach the top.

Each time you can either climb ```1``` or ```2``` steps. In how many distinct ways can you climb to the top?  
  
 

>Example 1:
```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```
>Example 2:
```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```
 

### Constraints:

- $1 <= n <= 45$
---
### Idea:
>我們可以把它當作下樓梯的問題，每一次我們可以選擇一格或是兩格，所以總共就會需要 ```n = (n-1) + (n-2)``` 次。接著我們需要利用動態規劃，把每一次計算的結果存在 list 中，就可以利用空間來減少計算量。
### Solution

```python=
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
```
