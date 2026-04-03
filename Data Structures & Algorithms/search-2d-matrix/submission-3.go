func searchMatrix(matrix [][]int, target int) bool {
    // find out where the element could possibly exist by checking
    // the first row of each element
    // if you found the row then apply binary search on it

    var rowIndex int = -1

    // we are not actually finding the target here
    // we are more about finding the array where target might exist

    // conditions
    // target <= row[i][o] && target >= row[i][len]

    left, right := 0, len(matrix)-1
    for left <= right {
        mid := (left + right)/2
        if matrix[mid][0] <= target && target <= matrix[mid][len(matrix[0]) - 1] {
            rowIndex = mid
            break
        } else if target > matrix[mid][0] {
            left = mid + 1
        } else {
            right = right - 1
        }
    }

    if rowIndex < 0 { 
        return false
    }

    left, right = 0, len(matrix[0])-1

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
