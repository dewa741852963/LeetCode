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
