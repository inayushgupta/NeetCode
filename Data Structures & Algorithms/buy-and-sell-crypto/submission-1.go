func maxProfit(prices []int) int {
    var maxProfit int

    for i, j := 0, 1; i < len(prices) - 1; i, j = i+1, j+1 {
        
        for k := j; k < len(prices); k++ {
            temp := prices[k] - prices[i]
            if temp > maxProfit {
                maxProfit = temp
            }
        }
    }
    return maxProfit
}
