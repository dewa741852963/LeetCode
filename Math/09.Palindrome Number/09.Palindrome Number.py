class Solution:
    import math
    def isPalindrome(self, x: int) -> bool:
        acc=0
        if x>10 :
            lenst = len(str(x))//2
            x_sp=list(str(x))
            for i in range(lenst):
                if x_sp[i]==x_sp[-(i+1)]:
                    acc+=1
                    if acc==lenst:
                        return True
                else:
                    return False
        elif 0<=x<10:
            return True
        else:
            return False

# //////////////////////////////best/////////////////////////////////////////
class Solution:
    import math
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x%10 == 0):   # if x is negative, return False. if x is positive and last digit is 0, that also cannot form a palindrome, return False.
            return False
        
        result = 0
        while x > result:
            result = result * 10 + x % 10
            x = x // 10
            
        return True if (x == result or x == result // 10) else False
