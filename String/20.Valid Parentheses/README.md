###### tags: `String`, `Stack`

# LeetCode 20.Valid Parentheses
Given a string s containing just the characters ```'('```, ```')'```, ```'{'```, ```'}'```, ```'['``` and ```']'```, determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.  
Open brackets must be closed in the correct order.  
Every close bracket has a corresponding open bracket of the same type.
  
  
 

>Example 1:
```
Input: s = "()"
Output: true
```

>Example 2:
```
Input: s = "()[]{}"
Output: true
```
>Example 3:
```
Input: s = "(]"
Output: false
```
 

### Constraints:

- $1 <= s.length <= 10^4$
- ```s``` consists of parentheses only ```'()[]{}'```.



---
### Idea:
>
### Solution

```python=
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i]=='(' or  s[i]=='[' or s[i]=='{':
                stack.append(s[i])
            elif len(stack)!=0:
                top = stack[-1]
                if top=='(':
                    if s[i]==')':
                        stack.pop()
                    else:
                        return False
                elif top=='[':
                    if s[i]==']':
                        stack.pop()
                    else:
                        return False
                elif top=='{':
                    if s[i]=='}':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            else:
                return False
        if stack==[]:
            return True
```
