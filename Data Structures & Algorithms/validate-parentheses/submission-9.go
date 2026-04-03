func isValid(s string) bool {
    // stack implimentation with slice
    var stack []rune = make([]rune, 0, len(s))

    for _, b := range s {
        if isOpening(b) {
            // append opening parenthesis to the stack
            stack = append(stack, b)
        } else {

            if len(stack) == 0 {
                return false
            }

            top := stack[len(stack) - 1]
            openingP := returnOpening(b)
            if top == openingP {
                // the opening parenthesis and closing one cancels out
                stack = stack[:len(stack) - 1]
            } else {
                return false
            }
        }
    }    
    return len(stack) == 0
}

func returnOpening(b rune) rune {
    switch b {
        case ']': return '['
        case '}' : return '{'
        case ')' : return '('
    }
    //this code will never run due to question guarantee
    return ' '
}

func isOpening(b rune) bool {
    return b == '[' || b == '{' || b == '('
}
