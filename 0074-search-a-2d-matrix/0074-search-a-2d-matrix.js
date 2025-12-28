/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    const rowCount = matrix.length
    const colCount = matrix[0].length
    let l = 0, r = ( rowCount * colCount ) - 1
    while(l <= r) {
        const mid = Math.floor((r + l) / 2)
        const rowInd = Math.floor( mid / colCount )
        const colInd = mid % colCount
        const numAtMid = matrix[rowInd][colInd]
        if (numAtMid == target) return true
        else if (numAtMid < target) {
            l = mid + 1
        }
        else {
            r = mid - 1
        }
    }

    return false
    
};