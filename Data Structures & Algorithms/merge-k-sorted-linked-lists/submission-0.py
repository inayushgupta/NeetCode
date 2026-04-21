# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        dummy = head = ListNode()
        heap = []

        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, id(l), l))

        while heap:
            _, _, node = heapq.heappop(heap)
            if node.next:
                heapq.heappush(heap, (node.next.val , id(node.next), node.next))

            head.next = node
            head = head.next

        return dummy.next      