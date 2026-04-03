func maxArea(h []int) int {
    maxArea := 0   
    left, right := 0, len(h)-1


    for left < right {
        dis := right - left
        area := min(h[left], h[right]) * dis
        maxArea = max(maxArea, area)
        if h[left] < h[right] {
            left=left+1
        } else {
            right=right-1
        }
    }
    
    return maxArea
}

func max(a, b int) int {
    if b > a {return b}
    return a
}

func min(a, b int) int {
    if b < a {return b}
    return a
}
