/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function(head) {
    if(!head) return 
    let slow = head, fast = head.next
    while(fast && fast.next) {
        slow = slow.next
        fast = fast.next.next
    }
    let secondHalf = slow.next
    slow.next = null

    // Revese the second half
    let prev = null, cur = secondHalf
    while(cur) {
        const temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    }
    secondHalf = prev

    // Join
    cur = head
    while(cur !== null && secondHalf !== null) {
        let temp1 = cur.next
        cur.next = secondHalf
        secondHalf = secondHalf.next
        cur.next.next = temp1
        cur = temp1
    }

};