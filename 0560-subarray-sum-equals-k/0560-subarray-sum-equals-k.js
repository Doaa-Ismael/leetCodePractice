/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function(nums, k) {
    let sum = 0, subArraySum = 0
    let prefixSumMap = {
        0: 1
    }
    for (let i = 0; i < nums.length; i++) {
        subArraySum += nums[i]
        let restSum = subArraySum - k
        if(prefixSumMap[restSum]) {
            sum += prefixSumMap[restSum]
        }
        prefixSumMap[subArraySum] = (prefixSumMap[subArraySum] || 0) + 1
    }
    return sum 
    
};