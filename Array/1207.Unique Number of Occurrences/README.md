###### tags: `Array`, `Hash Table`

# LeetCode 1207.Unique Number of Occurrences
Given an array of integers ```arr```, return ```true``` if the number of occurrences of each value in the array is unique or ```false``` otherwise.  
  
 

>Example 1:
```
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
```
>Example 2:
```
Input: arr = [1,2]
Output: false
```
>Example 3:
```
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
```
 

### Constraints:

- $1 <= arr.length <= 1000$
- $-1000 <= arr[i] <= 1000$
---
### Idea:
>先計算每一個數字出現的次數，並且存放到 list 中，再用 set 刪除相同出現的次數，最後比較 list 和 原先的arr 的長度就可以知道有沒有出現相同次數的數字。  
>
### Solution

Python:
```python=
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = []
        se = list(set(arr))
        for i in range(len(se)):
            count.append(arr.count(se[i]))
        se_count = set(count)
        if len(se_count) == len(count):
            return True
        elif len(se_count) != len(count):
            return False
```

C++
```cpp=
```

