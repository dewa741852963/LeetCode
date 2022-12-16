###### tags: `Math`, `String`, `Bit Manipulation`, `Simulation`

# LeetCode 67.Add Binary
Given two binary strings ```a``` and ```b```, return their sum as a binary string.  
  
 

>Example 1:
```
Input: a = "11", b = "1"
Output: "100"
```

>Example 2:
```
Input: a = "1010", b = "1011"
Output: "10101"
```

 

### Constraints:

- $1 <= a.length, b.length <= 10^4$
- ```a``` and ```b``` consist only of ```'0'``` or ```'1'``` characters.
- Each string does not contain leading zeros except for the zero itself.



---
### Idea:
>
### Solution

```python=
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
```
