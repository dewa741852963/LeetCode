###### tags: `Array`, `Binary Search`

# LeetCode 35.Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with ```O(log n)``` runtime complexity.  


>Example 1:
```
Input: nums = [1,3,5,6], target = 5
Output: 2
```
>Example 2:
```
Input: nums = [1,3,5,6], target = 2
Output: 1
```
>Example 3:
```
Input: nums = [1,3,5,6], target = 7
Output: 4
```
 

### Constraints:

- $1 <= nums.length <= 10^4$
- $-10^4 <= nums[i] <= 10^4$
- ```nums``` contains distinct values sorted in ascending order.
- $-10^4 <= target <= 10^4$
---
### Idea:
>
### Solution:

Python:
```python=
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        k = len(nums)//2
        if k==0:
            if nums[0] >= target:
                return 0
            else:
                return 1
        if nums[k] > target:
            for i in range(k):
                if nums[i] >= target:
                    return 0
                if nums[i] < target and nums[i+1] >= target:
                    return i+1
        elif nums[k] == target:
            return k
        else:
            for i in range(k,len(nums)-1,1):
                if nums[i] < target and nums[i+1] >= target:
                    return i+1
            return len(nums) 
        
```
Python be
```python=
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        k = len(nums)//2
        if k==0:
            if nums[0] >= target:
                return 0
            else:
                return 1
        if nums[k] > target:
            for i in range(k):
                if nums[i] >= target:
                    return 0
                if nums[i] < target and nums[i+1] >= target:
                    return i+1
        elif nums[k] == target:
            return k
        else:
            for i in range(k,len(nums)-1,1):
                if nums[i] < target and nums[i+1] >= target:
                    return i+1
            return len(nums) 
        
```
C++:
```cpp=
```