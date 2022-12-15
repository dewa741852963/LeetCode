class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ina = int(a)
        inb = int(b)
        k=0
        c = str(ina+inb)
        for i in range(len(c)-1,-1,-1):
            k+=1
            if c[i]=='2':
                c = c[:i] + '0' + c[i+1:]
                inc = int(c)
                inc += 1*10**k
                c = str(inc)
            elif c[i]=='3':
                c = c[:i] + '1' + c[i+1:]
                inc = int(c)
                inc += 1*10**k
                c = str(inc)
        return c
        
