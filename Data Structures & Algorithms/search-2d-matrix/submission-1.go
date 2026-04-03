func searchMatrix(matrix [][]int, target int) bool {
    // find out where the element could possibly exist by checking
    // the first row of each element
    // if you found the row then apply binary search on it

    var rowIndex int

    for i, j := range matrix {
        if j[0] <= target && j[len(j) - 1] >= target {
            rowIndex = i
            break
        }
    }


    left, right := 0, len(matrix[0])-1

    for left <= right {
        mid := (left + right)/2

        if matrix[rowIndex][mid] > target {
            right = mid - 1
        } else if matrix[rowIndex][mid] < target {
            left = mid + 1
        } else {
            return true 
        }
        
    }
    
    return false
}
