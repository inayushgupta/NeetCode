func topKFrequent(nums []int, k int) []int {
    freq := make(map[int]int)
    bucket := make([][]int, len(nums)+1)

    for _, n := range nums {
        freq[n]++
    }

    fmt.Println(freq)

    for key, value := range freq {
        fmt.Println(key, value, "executed", len(bucket), cap(bucket))
        bucket[value] = append(bucket[value], key)
        fmt.Println(bucket)
    }

    fmt.Println("hello")

    var result = []int{}

    for i := len(bucket)-1; i >= 0; i-- {
        for _, v := range bucket[i] {
            result = append(result, v)
            if len(result) == k {
                return result
            }
        }
    }

    return result

}
