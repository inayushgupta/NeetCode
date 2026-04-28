# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return None
        
        dummy = prev = ListNode(0, head)
        curr = head

        while curr:
            count = 1

            while curr and count < k:
                curr = curr.next
                count += 1
            
            if not curr:
                break
            
            nprev, ncurr = prev.next, curr.next
            check = curr

            while prev.next != check:
                node = prev.next
                prev.next = node.next
                node.next = curr.next
                curr.next = node

            prev, curr = nprev, ncurr

        return dummy.next
            
            