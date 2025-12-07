/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    const numsSet = new Set()
    let i = 0
    let res = 0

    nums.forEach(num => numsSet.add(num))

    for(num of numsSet) {
        if(!numsSet.has(num - 1)){
            let x = num + 1
           while(numsSet.has(x)){
            x = x + 1
           }
           res = Math.max(x - num, res)
        }
        
    }
    return res
    
};