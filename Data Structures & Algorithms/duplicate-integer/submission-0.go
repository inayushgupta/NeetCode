func hasDuplicate(nums []int) bool {
    var seen = make(map[int]bool)
    for _, num := range nums {
        if _, found := seen[num]; found {
            return true
        } else {
            seen[num] = true
        }
    }
    return false
}
