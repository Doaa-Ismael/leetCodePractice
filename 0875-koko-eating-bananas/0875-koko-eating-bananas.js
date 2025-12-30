/**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 */
var minEatingSpeed = function(piles, h) {
    const maxPileCount = piles.reduce((acc, cur) => acc < cur ? cur : acc, 0)
    let l = 1, r = maxPileCount
    let res = Number.MAX_SAFE_INTEGER
    while(l <= r) {
        const k = l + Math.floor(( r - l) / 2)
        const totalHours = piles.reduce((acc, cur) => {
            acc += Math.ceil(cur / k)
            return acc
        }, 0)
        
        if (totalHours <= h ) {
            res = Math.min(res, k)
            r = k - 1
        }
        else {
            l = k + 1
        }
    }
    return res
};