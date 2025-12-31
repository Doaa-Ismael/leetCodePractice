/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    if(nums[0] <= nums[nums.length - 1]) return nums[0]
    let l = 0, r = nums.length - 1
    while(l <= r) {
        const mid = l + Math.floor((r - l) / 2)
        if (nums[mid] < nums[r]) {
            r = mid
        }
        else {
            l = mid + 1
        }

        // if(nums[mid] < nums[l]) {
        //     r = mid
        // }
        // else if (nums[mid] > nums[r]) {
        //     l = mid + 1
        // }
        // else if (nums[mid] < nums[r]) {
        //     r = mid
        // }
        // else {
        //     break
        // }
    }
    const mid = l + Math.floor((r - l) / 2)
    return nums[mid]
    
};