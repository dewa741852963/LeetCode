class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        x = ['a','e','i','o','u']
        s = s.lower()
        count=0
        p =len(s)//2
        for i in range(p):
            if s[i] in x:
                count+=1
        for k in range(p,len(s)):
            if s[k] in x:
                count-=1
        if count==0:
            return True
        else:
            return False
        
