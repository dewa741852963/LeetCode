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
			
			


### Dynamic Solution
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