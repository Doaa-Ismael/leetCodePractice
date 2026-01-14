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
    if(head === null) return null
    let newHead = head
    const rest = reverseList(head.next) 
    if(rest) 
        newHead = rest
    if(head.next)
        head.next.next = head
    head.next = null
    return newHead
};

