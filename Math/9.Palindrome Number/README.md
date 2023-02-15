###### tags: `Math`

# LeetCode 9.Palindrome Number
Given an integer ```x```, return ```true``` if ```x``` is a
palindrome, and ```false``` otherwise.  

>Example 1:
```
IInput: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
```
>Example 2:
```
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```
>Example 3:
```
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```
 

### Constraints:

- $-2^{31} <= x <= 2^{31} - 1$
---
### Idea:
>
### Solution

Python:
```python=
class Solution:
    import math
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x%10 == 0):   
            return False
        result = 0
        while x > result:
            result = result * 10 + x % 10
            x = x // 10
        return True if (x == result or x == result // 10) else False
```

C++
```cpp=
```
