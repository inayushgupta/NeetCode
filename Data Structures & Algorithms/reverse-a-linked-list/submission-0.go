/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reverseList(head *ListNode) *ListNode {
    var reverse *ListNode

    for head != nil {
        next := head.Next
        head.Next = reverse
        reverse = head
        head = next
    }

    return reverse
}
