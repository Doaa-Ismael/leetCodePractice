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
    
    for (let i = 0; i < tokens.length; i++) {
        if(operators[tokens[i]]) {
            const num1 = stack.pop()
            const num2 = stack.pop()
            const newNum = calc(num2, num1, tokens[i])
            stack.push(newNum)
        }
        else  {
            stack.push(Number(tokens[i]))
        }
    }
    return stack.pop()
};