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
    const arr = []
    let cur = head
    while(cur) {
        arr.push(cur)
        cur = cur.next
    }
    let i = 0, j = arr.length - 1
    cur = {}
    while( i <= j) {
        cur.next = arr[i]
        cur.next.next = null
        if(i == j) return 
        i++
        cur.next.next = arr[j]
        cur = cur.next.next
        cur.next = null
        j--
    }
};