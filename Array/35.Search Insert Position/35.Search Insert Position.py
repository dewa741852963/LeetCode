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
