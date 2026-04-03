func longestConsecutive(nums []int) int {
    longest := 0
    exists := make(map[int]bool)

    for _, n := range nums {
        exists[n] = true
    }

    for _, n := range nums {
        //check if the left neighbour exists or not
        if exists[n-1] {
            continue
        } else {
            newLong := 1
            curr := n+1
            for exists[curr] {
                newLong++
                curr++
            }
            if newLong > longest {
                longest = newLong
            }
        }
    }
    return longest
}
