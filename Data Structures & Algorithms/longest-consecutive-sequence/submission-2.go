func longestConsecutive(nums []int) int {
    longest := 0
    exists := make(map[int]struct{})

    for _, n := range nums {
        exists[n] = struct{}{}
    }

    for n := range exists {
        if _, ok := exists[n-1]; ok {
            continue
        } else {
            newLong := 1
            curr := n + 1
            for {
                if _, ok := exists[curr]; ok {
                newLong++
                curr++
                } else {
                    break
                }
            }
            if newLong > longest {
                longest = newLong
            }
        }
    }
    return longest
}
