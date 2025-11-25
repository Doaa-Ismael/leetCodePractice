/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = function(s1, s2) {
    if(s1.length > s2.length) return false

    const arr1 = new Array(26).fill(0), arr2 = new Array(26).fill(0)
    let matches = 0

    for (let i = 0; i < s1.length; i++) {
        arr1[s1.charCodeAt(i) - 97] = arr1[s1.charCodeAt(i) - 97] + 1
        arr2[s2.charCodeAt(i) - 97] = arr2[s2.charCodeAt(i) - 97] + 1
    }
    arr1.forEach((_, i) => {
        if(arr1[i] === arr2[i])
            matches++
    })
    for (let r = s1.length; r < s2.length; r++) {
        if(matches == 26) return true
        let rightIndex = s2.charCodeAt(r) - 97
        let leftIndex = s2.charCodeAt(r - s1.length) - 97

        
        if(arr1[rightIndex] == arr2[rightIndex])
            matches--
        arr2[rightIndex]+=1
        if (arr1[rightIndex]== arr2[rightIndex])
            matches++

        
        if(arr1[leftIndex] === arr2[leftIndex])
            matches--
        arr2[leftIndex]-=1
        if(arr1[leftIndex]== arr2[leftIndex])
            matches++
    }

    if(matches == 26) return true

    return false
    
};