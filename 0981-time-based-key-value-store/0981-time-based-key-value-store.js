
var TimeMap = function() {
    this.keysMap = {}
};

/** 
 * @param {string} key 
 * @param {string} value 
 * @param {number} timestamp
 * @return {void}
 */
TimeMap.prototype.set = function(key, value, timestamp) {
    this.keysMap[key] = this.keysMap[key] || []
    this.keysMap[key].push({ value, timestamp })
};

const binarySearch = (arr, target) => {
    let l = 0, r = arr.length - 1, ans = null
    while(l <= r) {
        const mid = l + Math.floor( (r - l ) / 2)
        if(arr[mid].timestamp <=  target)  {
            ans = mid
            l = mid + 1
        }
        else {
            r = mid - 1
        }
    }
    return ans
}


/** 
 * @param {string} key 
 * @param {number} timestamp
 * @return {string}
 */
TimeMap.prototype.get = function(key, timestamp) {
    if(!this.keysMap[key]) return ""
    const sortedArray = this.keysMap[key]
    const res = binarySearch(sortedArray, timestamp)
    if(res === null) return ""
    return sortedArray[res].value
};

/** 
 * Your TimeMap object will be instantiated and called as such:
 * var obj = new TimeMap()
 * obj.set(key,value,timestamp)
 * var param_2 = obj.get(key,timestamp)
 */