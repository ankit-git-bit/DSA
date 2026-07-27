class Solution:
    def isValid(self, s: str) -> bool:
        stack1=[]
        i=0
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                stack1.append(s[i])
            else:
                if not stack1:
                    return False
                top=stack1.pop()
                if s[i]==')' and top!='(':
                    return False
                if s[i]==']' and top!='[':
                    return False
                if s[i]=='}' and top!='{':
                    return False
        return len(stack1)==0