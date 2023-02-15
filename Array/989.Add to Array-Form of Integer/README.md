###### tags: `Array`, `Math`

# LeetCode 989.Add to Array-Form of Integer
he array-form of an integer ```num``` is an array representing its digits in left to right order.

- For example, for num = ```1321```, the array form is ```[1,3,2,1]```.

Given ```num```, the array-form of an integer, and an integer k, return the array-form of the integer ```num + k```.  
  
 

>Example 1:
```
Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
```
>Example 2:
```
Input: num = [2,7,4], k = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
```
>Example 3:
```
Input: num = [2,1,5], k = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021
```
 

### Constraints:

- $1 <= num.length <= 10^4$
- $0 <= num[i] <= 9$
- ```num``` does not contain any leading zeros except for the zero itself.
- $1 <= k <= 10^4$
---
### Idea:
>num 加上 array 最後一個數字之後除以10，就會是 array 最後一個位子的數值，以此類推。如果最後 num 還有數值，就會把 num 值放到 array 的最前面。
### Solution:

Python:
```python=
class Solution:
  def addToArrayForm(self, num: List[int], k: int) -> List[int]:
    for i in reversed(range(len(num))):
      k, num[i] = divmod(num[i] + k, 10)

    while k > 0:
      num = [k % 10] + num
      k //= 10

    return num
```

C++:
```cpp=
class Solution 
{
 public:
  vector<int> addToArrayForm(vector<int>& num, int k) 
  {
    for (int i = num.size() - 1; i >= 0; --i) 
    {
      num[i] += k;
      k = num[i] / 10;
      num[i] %= 10;
    }
    while (k > 0) {
      num.insert(begin(num), k % 10);
      k /= 10;
    }
    return num;
  }
};
```