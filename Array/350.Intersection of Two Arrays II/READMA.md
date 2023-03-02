###### tags: `Array`, `Two Pointers`, `Binary Search`, `Sorting`

# 350.Intersection of Two Arrays II
Given two integer arrays `nums1` and `nums2`, return _an array of their intersection_. Each element in the result must appear as many times as it shows in both arrays and you may return the result in **any order**.
  
 

>Example 1:
```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
```
>Example 2:
```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
```
>Example 3:
```
Input: nums = [3,3], target = 6
Output: [0,1]
```
 

### Constraints:

- $1 <= nums1.length, nums2.length <= 1000$
- $0 <= nums1[i], nums2[i] <= 1000$
---


### Idea:
>我們先把 array 進行排序，並且比較 array 的大小，小的為k2，大的為k1。
>一開始比較 k1 和 k2 的第一個數值，如果相等，存放到 v 中，並且 k1 和 k2 往下一個數值比較；如果 k1 >k2 那我們就查看 k2 下一個的數值；如果 k1<k2 那我們就查看 k1 下一個的數值，直到結束。
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