# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1=[]
        curr=list1
        while curr:
            l1.append(curr.val)
            curr = curr.next
        l2=[]
        cur=list2
        while cur:
            l2.append(cur.val)
            cur = cur.next
        
        l3=l1+l2
        l3.sort()
        dummy = ListNode(0)
        curr=dummy
        for i in l3:
            curr.next=ListNode(i)
            curr=curr.next
        return dummy.next
        
