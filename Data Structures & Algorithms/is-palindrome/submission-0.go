func isPalindrome(s string) bool {
    isPal := true
    for left, right := 0, len(s)-1; left < right; left, right = left+1, right-1 {
        
        leftElement, lis := isAlpha(rune(s[left]))
        rightElement, ris := isAlpha(rune(s[right]))
        
        if !lis {
            right++
            continue
        }
    // this way the index remain the same until alpha is found 
        if !ris {
            left--
            continue 
        }

        if leftElement != rightElement {
            isPal = false
        }
    } 
    return isPal
}

func isAlpha(c rune) (rune, bool) {
    switch {
    case 'a' <= c && c <= 'z':
        return c, true
    case 'A' <= c && c <= 'Z':
        return unicode.ToLower(c), true
    case '0' <= c && c <= '9':
        return c , true
    }
    return c, false
}

func ConvertToLower() {

}