/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteMiddle = function(head) {
    if(!head || !head.next) return null

    let slow = head, fast = head.next
    while(fast && fast.next) {
        slow = slow.next
        fast = fast.next.next
    }
    let mid = (fast == null) ? slow : slow.next
    let cur = head
    while(cur) {
        if(cur.next == mid) {
            cur.next = cur.next.next
            break
        }
        cur = cur.next
    }
    return head
};