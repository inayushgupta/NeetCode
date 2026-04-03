func isValid(s string) bool {
    var stack []rune

    for _, b := range s {
        if b == '(' || b == '{' || b == '[' {
            stack = append(stack, b)
        } else {
            if len(stack) == 0 {
                stack = append(stack, b)
                break
            }

            if stack[len(stack) - 1] == GetOpeningBracket(b) {
                stack = stack[:len(stack) - 1]
            } else {
                break
            }
        }
    }
    return len(stack) == 0
}

func GetOpeningBracket(b rune) rune {
    switch b {
        case ')': return '('
        case '}': return '{'
        case ']': return '['
    }
// this code will never run due to question guarantee
    return ' '
}