/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
    let currnet = head
    while(currnet !== null) {
        if(currnet.visited) return true
        currnet.visited = true
        currnet = currnet.next
    }
    return false
    
};