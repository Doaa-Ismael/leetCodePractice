/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    if(nums[0] <= nums[nums.length - 1]) return nums[0]
    let l = 0, r = nums.length - 1, ans = Number.MAX_SAFE_INTEGER
    while(l <= r) {
        const mid = l + Math.floor((r - l) / 2)
        if (nums[mid] < nums[l]) {
            ans = Math.min(ans, nums[mid])
            r = mid
        }
        else {
            ans = Math.min(ans, nums[l])
            l = mid + 1
        }
    }
    return ans
    
};
