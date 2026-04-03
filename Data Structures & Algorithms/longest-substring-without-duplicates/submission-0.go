func lengthOfLongestSubstring(s string) int {
    
    if len(s) == 0 {return 0}
    
    last := make(map[byte]int)

    longest, left := 0, 0

    for right := 0; right < len(s); right++ {
        
        c := s[right]

        if idx, ok := last[c]; ok && idx > left {
            left = idx
        }

        length := right-left+1
        if length > longest {longest = length}

        last[c] = right+1
    }
    return longest
}
