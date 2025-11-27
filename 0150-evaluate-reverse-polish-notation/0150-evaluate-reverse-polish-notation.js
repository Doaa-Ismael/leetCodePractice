/**
 * @param {string[]} tokens
 * @return {number}
 */
const calc = (num1, num2, op) => {
    if(op === '+') return parseInt(num1+num2)
    if(op === '-') return parseInt(num1-num2)
    if(op === '*') return parseInt(num1*num2)
    if(op === '/') return parseInt(num1/num2)
}

var evalRPN = function(tokens) {
    const stack = []
    const operators = {
        "+": true,
        "-": true, 
        "*": true, 
        "/": true
    }
    
    let i = tokens.length - 1
    while(true && i >= 0) {
        if(operators[tokens[i]]) {
            stack.push(tokens[i])
        }
        else {
            if(operators[stack[stack.length - 1]])
                stack.push(tokens[i])

            else {
                console.log(stack)
                res = Number(tokens[i])
                while(stack.length >= 2 && !operators[stack[stack.length - 1]]) {
                    const num = stack.pop()
                    const operator = stack.pop()
                    res = calc(res, Number(num), operator)
                }
                console.log({res, stack: [...stack]})
                stack.push(res)
            }
        }
        i--
    }
    return stack.pop()
};