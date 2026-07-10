class Solution:
    def isHappy(self, n: int) -> bool:
        def square(n):
            ans=0
            while n>0:
                x=n%10
                ans+=x*x
                n=n//10
            return ans
        slow=n
        fast=square(n)
        while(slow!=fast):
            slow=square(slow)
            fast=square(square(fast))
        return slow==1

        