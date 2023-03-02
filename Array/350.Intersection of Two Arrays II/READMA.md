###### tags: `Array`, `Two Pointers`, `Binary Search`, `Sorting`

# 350.Intersection of Two Arrays II
Given two integer arrays `nums1` and `nums2`, return _an array of their intersection_. Each element in the result must appear as many times as it shows in both arrays and you may return the result in **any order**.
  
 

>Example 1:
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```
>Example 2:
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```
>Example 3:
```
Input: nums = [3,3], target = 6
Output: [0,1]
```
 

### Constraints:

- $2 <= nums.length <= 10^4$
- $-10^9 <= nums[i] <= 10^9$
- $-10^9 <= target <= 10^9$
- Only one valid answer exists.
---


### Idea:
>我們先把 array 進行排序，並且比較 array 的大小，小的為k2，大的為k1。
>一開始比較 k1 和 k2 的第一個數值，如果相等，存放到 v 中，並且往下一個數值比較；如果 k1 >k2 那我們就查看k2的下一個
### Solution:

Python:
```python=
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
```

C++:
```cpp=
```