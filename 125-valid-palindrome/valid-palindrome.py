class Solution:
    def isPalindrome(self, s: str) -> bool:
        text= "".join([char for char in s if char.isalnum()])
        text_lower=text.lower()
        l=0
        r=len(text_lower)-1
        while l<r:
            if text_lower[l]!=text_lower[r]:
                return False
            l+=1
            r-=1
        return True
