

function binarySearch (nums, target, l, r) {
    if(r < l) return -1
    if(l == r) return target === nums[l] ? l : -1
    const mid = Math.floor((l + r) / 2)
    if(target === nums[mid]) return mid
    else if (target < nums[mid]) return binarySearch(nums, target, l, mid - 1)
    else return binarySearch(nums, target, mid + 1, r)
}

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {

    const result = binarySearch(nums, target, 0, nums.length - 1)
    return result
    
};