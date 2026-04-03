func isValid(s string) bool {
    var parse  = []rune{}

    for _, b := range s {
        b = rune(b)
        if b == '{' || b == '[' || b == '(' {
            parse = append(parse, b)
        } else {
            
            if len(parse) == 0 {
                parse = append(parse, b)
                break;
            }
            
            var lastelementoflist = parse[len(parse) - 1]
            if lastelementoflist == returnCompliment(b) {
                parse = parse[:len(parse) - 1]
                continue
            } else {
                break
            }
        }
    }
    return len(parse) == 0
}

func returnCompliment(b rune) rune {
    switch b {
        case '}': return '{'
        case ')': return '('
        default: return '['
    }
}