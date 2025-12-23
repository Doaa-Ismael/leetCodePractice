/**
 * @param {number} target
 * @param {number[]} position
 * @param {number[]} speed
 * @return {number}
 */
var carFleet = function(target, position, speed) {
    const positionsWithSpeed = position.map((p, i) => [p, speed[i]]).sort((a, b) => b[0] - a[0])
    let result = 1
    let prevTimeToDest = (target - positionsWithSpeed[0][0])/ positionsWithSpeed[0][1]
    for(let i = 1 ;  i < positionsWithSpeed.length ; i++) {
        const timeToDest = (target - positionsWithSpeed[i][0])/ positionsWithSpeed[i][1]
        if(timeToDest > prevTimeToDest) {
            result+=1
            prevTimeToDest = timeToDest
        } 
    }

    return result
    
};