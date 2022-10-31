# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        list = head
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                list.next = ListNode(list1.val)
                list1 = list1.next
            else:
                list.next = ListNode(list2.val)
                list2 = list2.next
            list = list.next
            
        while list1 is not None:
            list.next = ListNode(list1.val)
            list1 = list1.next
            list = list.next
        while list2 is not None:
            print(list2.val)
            list.next = ListNode(list2.val)
            list2 = list2.next
            list = list.next
           
        return head.next
        