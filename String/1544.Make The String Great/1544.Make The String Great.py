class Solution:
    def makeGood(self, s: str) -> str:
        if s.islower() or s.isupper() or s=='':
            a=0
        else:
            a=2
            k = len(s)
        while a>1:
            for i in range(len(s)-1):
                if s[i].islower():
                    if s[i+1] == s[i].upper():
                        s = s[:i]+s[i+2:]
                        break
                else:
                    if s[i+1] == s[i].lower() :
                        s = s[:i]+s[i+2:]
                        break 
            k-=1
            if s.islower() or s.isupper() or s=='' or k==0:
                a=0
        return s
        

# //////////////////////////////best/////////////////////////////////////////
class Solution:
    def makeGood(self, s: str) -> str:
        result = []
        for c in s:
            if not result:
                result.append(c)
            elif result[-1].isupper() and result[-1].lower() == c:
                result.pop()
            elif result[-1].islower() and result[-1].upper() == c:
                result.pop()
            else:
                result.append(c)
        return ''.join(result)
