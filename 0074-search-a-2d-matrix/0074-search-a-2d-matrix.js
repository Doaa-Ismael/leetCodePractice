/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    let l = 0, r = matrix.length - 1, colsCount = matrix[0].length - 1
    let rowIndex
    for (let i = 0; i < matrix.length ; i++) {
        if(matrix[i][0]  <= target && matrix[i][colsCount] >= target) {
            rowIndex = i
            break;
        }

    }
    if(rowIndex == null) return false
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