func threeSum(nums []int) [][]int {
    groups := make([][]int, 0)
    
    // sort the array
    sort.Slice(nums, func(i, j int) bool {
        return nums[i] < nums[j]
    })

    for i, _ := range nums {
        left := i+1
        right := len(nums)-1
         if i > 0 && nums[i] == nums[i-1] {
            continue
            }    
        for left < right {
       
            total := nums[i] + nums[left] + nums[right]

            switch {
                case total > 0: {
                    right -= 1
                }
                case total < 0: {
                    left += 1
                }
                default: {
                    groups = append(groups, []int{nums[i], nums[left], nums[right]})

                    for left < right && nums[left] == nums[left+1] {
                        left++
                    }
                    for left < right && nums[right] == nums[right-1] {
                        right--
                    }
                    left++
                    right--
                }
            
            }    
        }
    }

    fmt.Println(nums)
    return groups
}
