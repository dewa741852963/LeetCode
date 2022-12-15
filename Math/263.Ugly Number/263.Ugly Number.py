class Solution:
    def isUgly(self, n: int) -> bool:
        if n==0:
            return False
        else:
            while(n != 0 and n != 1):
                if n % 2 == 0:
                    n = n / 2
                    continue 
                elif n % 3 == 0:
                    n = n / 3
                    continue
                elif n % 5 == 0:
                    n = n / 5
                    continue
                else:
                    return False
            return True
