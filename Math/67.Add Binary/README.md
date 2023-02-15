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
>我們可以把把每一個為
### Solution:

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
最佳解：
```python=
class Solution:
  def addBinary(self, a: str, b: str) -> str:
    s = []
    carry = 0
    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 or j >= 0 or carry:
      if i >= 0:
        carry += int(a[i])
        i -= 1
      if j >= 0:
        carry += int(b[j])
        j -= 1
      s.append(str(carry % 2))
      carry //= 2

    return ''.join(reversed(s))
    
```
c++ 解法
```cpp=
class Solution {
public:
    // Function to add two binary numbers represented as strings
    string addBinary(string a, string b) {
        // Initialize two pointers to traverse the binary strings from right to left
        int i = a.length()-1;
        int j = b.length()-1;
        string ans;
        int carry = 0;
        
        // Loop until both pointers have reached the beginning of their respective strings and there is no carry-over value left
        while(i >= 0 || j >= 0 || carry) {
            // Add the current binary digit in string a, if the pointer is still within bounds
            if(i >= 0) {
                carry += a[i] - '0';//char 轉換成 int
                i--;
            }
            
            // Add the current binary digit in string b, if the pointer is still within bounds
            if(j >= 0) {
                carry += b[j] - '0';//char 轉換成 int
                j--;
            }
            
            // Calculate the next binary digit in the result by taking the remainder of the sum divided by 2
            ans += (carry % 2 + '0');//int 轉換成 char
            
            // Calculate the next carry-over value by dividing the sum by 2
            carry = carry / 2;
        }
        
        // Reverse the result and return it as a string
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
```