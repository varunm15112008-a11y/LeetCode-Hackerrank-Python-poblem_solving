class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        sum=0
        rem=0
        while(num>0):
            rem=num%10
            sum=sum*10+rem
            num=num//10
        if (x == sum):
            return True
        else:
            return False
