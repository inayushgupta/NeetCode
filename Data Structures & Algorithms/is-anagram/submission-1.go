func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }

    var frequency = [26]int{}

    for i := 0; i < len(s); i++ {
        frequency[s[i]-'a']++
        frequency[t[i]-'a']--
    }

    for _, count := range frequency {
        if count != 0 {
            return false
        }
    }

    return true
}
