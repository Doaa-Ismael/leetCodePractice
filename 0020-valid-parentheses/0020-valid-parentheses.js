/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const stack = []
    const parentheses = {
        '(' : ')',
        '[' : ']',
        '{' : '}'
    }

    for (let i = 0; i < s.length; i++) {
        if(parentheses[s[i]]) {
            stack.push(parentheses[s[i]])
        }
        else {
            if(s[i] === stack[stack.length - 1]) {
                stack.pop()
            }
            else return false
        }
    }
    if(stack.length > 0 ) return false

    return true
    
};