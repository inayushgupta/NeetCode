# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)

        prev = dummy
        curr = head
        kx = 1

        while curr:
            kx = 1

            while curr and kx < k:
                curr = curr.next
                kx += 1
            
            if curr == None:
                break
            
            prev_new = prev.next
            curr_new = curr.next

            while kx != 1:
                node = prev.next
                node_next = node.next
                
                node.next = None
                prev.next = node_next
                
                curr_next = curr.next
                curr.next = node

                node.next = curr_next
                kx -= 1
            
            curr = curr_new
            prev = prev_new
            

            # there are three cases
            """
            1. when there are still elements left
            2. when the elements are insufficient
            3. when the curr = None
                -> do a normal reverse

                    if not curr and kx == 3: # reverse normally and attach
            
            reverse = None
            curr = prev.next
            prev.next = None

            while curr:
                nex = curr.next
                curr.next = reverse
                reverse = curr
                curr = nex

            prev.next = reverse
            """

        return dummy.next