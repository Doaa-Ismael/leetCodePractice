/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let l = 0, r = nums.length - 1
    while(l <= r) {
        const mid = l + Math.floor((r - l) / 2)
        if(nums[mid] === target) return mid
        // left array is sorted and the target is within it
        else if (nums[mid] >= nums[l]) {
            if(nums[l] <= target && target <= nums[mid])
                r = mid - 1
            else 
                l = mid + 1
        }
        else {
            if(nums[mid+1] <= target && nums[r] >= target)
                l = mid + 1
            else 
                r = mid - 1
        }
    }
    return -1
};