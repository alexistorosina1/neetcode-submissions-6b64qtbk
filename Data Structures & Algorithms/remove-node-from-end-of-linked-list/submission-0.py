# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # find the starting point of the right pointe
        while n > 0:
            right = right.next
            n -= 1
        # find the node to delete
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy.next