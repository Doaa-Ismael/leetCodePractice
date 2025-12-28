/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    let top = 0, bottom = matrix.length - 1, cols = matrix[0].length, mid
    while(top <= bottom) {
        mid = Math.floor( (top + bottom) / 2 )
        if (matrix[mid][0] > target ) {
            bottom = mid - 1
        }
        else if (matrix[mid][cols - 1] < target) {
            top = mid + 1
        }
        else {
            break;
        }
    }
    if (!(top <= bottom)) return false
    let l = 0, r = cols - 1
    let row =  mid
    while(l <= r) {
        mid = Math.floor( (l + r) / 2 )
        if(target < matrix[row][mid])
            r = mid - 1
        else if (target == matrix[row][mid]) 
            return true
        else 
            l = mid + 1
    }
    
    return false
};