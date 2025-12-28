/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
    let l = 1, r = x - 1
    if(x == 1 || x === 0) return x
    while(l <= r) {
        let mid =  Math.floor((l+r) / 2)
        if (mid*mid == x) return mid
        else if (mid*mid < x && ((mid+1) * (mid + 1)) > x ) return mid
        else if (mid*mid > x) r = mid - 1
        else if (mid*mid < x ) l = mid + 1
    }
    
};