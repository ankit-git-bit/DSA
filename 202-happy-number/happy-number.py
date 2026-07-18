class Solution:
    def isHappy(self, n: int) -> bool:
        s=set()

        while n!=1:
            if n in s:
                return False
            s.add(n)
            v1=0
            var=0
            while n>0:
                a=n%10
                var=a*a
                v1+=var
                n=n//10
            n=v1
        return True
