class Solution:
    def romanToInt(self, s: str) -> int:
        twokey = ['IV','IX','XL','XC','CD','CM']
        key={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        splits=len(s)
        add=[]
        total =0
        for i in range(splits):
            if i < splits-1:
                if s[i:i+2] in twokey:
                    add.append(0)
                else:
                    add.append(1)
            else:
                add.append(1)

        for i in range(splits):
            m2=key[str(s[i])]
            mit=add[i]
            if mit==1:
                total=total+m2
            elif mit==0:
                total=total-m2
        return total
                    
