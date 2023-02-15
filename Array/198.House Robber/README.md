###### tags: `Array`, `Dynamic Programming`

# LeetCode 198. House Robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array ```nums``` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.  
  
 

>Example 1:
```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```
>Example 2:
```
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
```

 

### Constraints:

- 1 <= nums.length <= 100
-  0 <= nums[i] <= 400
---
### Idea:
>如果只有一家那我們沒有選擇只能是那一家；如果有兩家的時候我們會選擇錢比較多的那一家；當我們有三家的時候此時就會需要比較 ==第一家加上第三家== 和 ==第二家== 哪一個比較大。
### Solution:

```python=
class Solution:
    def rob(self, nums: List[int]) -> int:
        total = []
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0],nums[1])
        elif len(nums)>2:
            total.append(nums[0])
            total.append(max(nums[0],nums[1]))
            for i in range(2,len(nums)):
                total.append(max(total[i-1],total[i-2] + nums[i]))
            return total[-1]
```


---
### Dynamic Idea:
> 我們可以利用動態規劃的方式，計算 ==前前家加上現在這一家== 和 ==前一家== 哪一個比較划算，就可以有效的節省空間了。

### Dynamic Solution

```python=
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0],nums[1])
        elif len(nums)>2:
            prevtwo = nums[0]
            prevone = nums[1]
            for i in range(2,len(nums)):
                new = max(prevtwo + nums[i], prevone)
                prevtwo = max(prevtwo, prevone)
                prevone = max(prevone, new)
            return max(prevtwo, prevone)
```