/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    const numsSet = new Set()
    let count = 0
    let i = 0
    let res = 0

    nums.forEach(num => numsSet.add(num))

    for(num of numsSet) {
        if(!numsSet.has(num - 1)){
            count = 1
            let x = num
           while(numsSet.has(x + 1)){
            count++
            x = x+1
           }
           res = Math.max(count, res)
        }
        
    }
    return res
    
};