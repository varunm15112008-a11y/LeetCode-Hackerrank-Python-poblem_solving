# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        L1 = []
        curr = l1
        while curr:
            L1.append(curr.val) 
            curr = curr.next
        
        L1r=L1[::-1]
        str1=''
        for i in L1r:
            str1+=str(i)
        num1=int(str1)
        
        L2 = []
        curr = l2
        while curr:
            L2.append(curr.val) 
            curr = curr.next
        
        L2r=L2[::-1]
        str2=''
        for i in L2r:
            str2+=str(i)
        num2=int(str2)

        num=num1+num2
        str3=str(num)

        dummy = ListNode(0)
        curr = dummy
        
        for digit in str3[::-1]:
            curr.next = ListNode(int(digit))
            curr = curr.next
            
        return dummy.next
        
