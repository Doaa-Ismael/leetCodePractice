/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function(nums, k) {
    let sum = 0
    let prefix = [0]
    for (let i = 0; i < nums.length ; i++) {
        prefix[i+1] = prefix[i] + nums[i]
    }
    for (let i = 0; i < nums.length ; i++) {
        let subArraySum = 0
        for (let j = i; j < nums.length; j++) {
            subArraySum = prefix[j+1] - prefix[i]
            if(subArraySum === k) {
                sum++
            }
        }
    }
    return sum 
    
};