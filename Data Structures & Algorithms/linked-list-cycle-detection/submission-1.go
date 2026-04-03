/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func hasCycle(head *ListNode) bool {
    // create map of values
    // if the next value gives the value already in the list
    // return true

    visited := make(map[*ListNode]bool)

    for head != nil {
        if visited[head] {
            return true
        } else {
            visited[head] = true
            head = head.Next
        }
    }
    return false
}
