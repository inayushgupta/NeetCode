func twoSum(nums []int, target int) []int {
    exists := make(map[int][]int) 

    for i, num := range nums {
        if index, ok := exists[target-num]; ok {
            return []int{index[0], i}
        } else {
            exists[num] = append(exists[num], i)
        }
    }
    return []int{}
}
