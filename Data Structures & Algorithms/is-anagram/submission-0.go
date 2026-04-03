func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }

    count := make(map[byte]int, len(s))

    for i, _ := range s {
        count[s[i]] = count[s[i]] + 1
        count[t[i]] = count[t[i]] - 1
    }

    for _, v := range count {
        if v != 0 {
            return false
        }
    }
    return true
}
