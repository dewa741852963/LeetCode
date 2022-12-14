class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        total = 0
        count = 0
        num = []
        for i in range(len(digits)-1,-1,-1):
            total += digits[i]*10**count
            count+=1
        tostr=str(total+1)
        for i in range(len(tostr)):
            num.append(tostr[i])
        return num
