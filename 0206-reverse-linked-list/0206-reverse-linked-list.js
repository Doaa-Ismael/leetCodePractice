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
var reverseList = function(head) {
    if(!head) return null
    let prev = null, cur = head, next = null
    while(cur != null) {
        const nextNode = cur.next
        cur.next = prev
        prev = cur
        cur = nextNode
    }
    return prev
};