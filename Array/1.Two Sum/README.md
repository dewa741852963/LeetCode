###### tags: `Array`

# 1.Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.  
  
 

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

     2 <= nums.length <= 104
     -109 <= nums[i] <= 109
     -109 <= target <= 109
     Only one valid answer exists.
---
### Idea:
> 把每一個 nums 中的數字先進行標記，接這用 target 減每一個 nums 中的數字就可以得到 complement ，接著再查看 complement 有沒有出現在過去的標記中，有出現就進行回傳，沒有繼續尋找直到全部找完。
### Solution:

Python:
```python
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
class Solution {

public:

    vector<int> twoSum(vector<int>& nums, int target) {

        unordered_map <int, int> mp;

  

        for (int i =0; i<nums.size(); i++){

            if (mp.find(target - nums[i]) == mp.end())

                mp[nums[i]] = i;

            else

                return {mp[target - nums[i]], i};

        }

        return {-1,-1};

    }

};
```