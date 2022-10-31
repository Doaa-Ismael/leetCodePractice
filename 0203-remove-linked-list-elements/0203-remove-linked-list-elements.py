# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        result_head = ListNode()
        result_tail = result_head
        cur = head
        
        while cur:
            if cur.val != val:
                result_tail.next = cur
                result_tail = result_tail.next
                cur = cur.next
                result_tail.next = None
            
            else:
                cur = cur.next
        
        
        return result_head.next