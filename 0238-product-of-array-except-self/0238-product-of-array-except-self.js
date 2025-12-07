/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    const prefix = new Array(nums.length + 2)
    const suffix = new Array(nums.length + 2)
    const answer = []

    prefix[0] = 1
    for (let i = 0; i < nums.length; i++)
        prefix[i+1] = prefix[i] * nums[i]
    
    suffix[nums.length + 1] = 1
    for (let i = nums.length - 1; i >= 0; i--)
        suffix[i+1] = suffix[i+2] * nums[i]

    for (let i = 0;  i < nums.length; i++) {
        answer.push(suffix[i+2] * prefix[i] )
    }
    
    return answer
    
};