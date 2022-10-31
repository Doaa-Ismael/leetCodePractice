# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size, ptr = 0, head
        
        while ptr is not None:
            size += 1
            ptr = ptr.next
        
        ptr = head
        node_index = size - n;
        
        if node_index == 0:
                return head.next
        
        for x in range(node_index- 1):
            ptr = ptr.next
        
        if ptr.next is not None:
            ptr.next = ptr.next.next
        
        return head
        