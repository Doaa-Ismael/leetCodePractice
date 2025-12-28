/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    let l = 0, r = matrix.length - 1, colsCount = matrix[0].length - 1
    let rowIndex
    while(l <= r) {
        const mid = Math.floor((r + l) / 2)
        const numAtMid = matrix[mid][0]
        if(numAtMid == target) return true
        if(numAtMid < target)  {
            l = mid + 1
        }
        else {
            r = mid - 1
        }
        if(r <= l ) rowIndex = r
        else rowIndex = l
    }
    if(rowIndex == null || rowIndex < 0 || rowIndex > matrix.length) return false
    l = 0, r = matrix[rowIndex].length - 1
    while(l <= r) {
        const mid = Math.floor((r + l) / 2)
        const numAtMid = matrix[rowIndex][mid]
        if(numAtMid == target) return true
        else if (numAtMid < target) l = mid + 1
        else r = mid - 1
    }
    return false
    
};