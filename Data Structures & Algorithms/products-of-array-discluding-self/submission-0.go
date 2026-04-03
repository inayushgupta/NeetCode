func productExceptSelf(nums []int) []int {
    res := make([]int, len(nums), len(nums))

    var reg int = 1
    //prefix
    for i, n := range nums {
        res[i] = reg
        reg = reg*n
    }
    //reset the register
    reg = 1
    //postfix
    for i := len(nums)-1; i >= 0; i-- {
        res[i] *= reg
        reg = reg*nums[i]
    }
    return res
}
