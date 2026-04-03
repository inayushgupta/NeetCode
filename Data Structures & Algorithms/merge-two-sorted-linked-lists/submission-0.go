/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
    list := &ListNode{0, nil}
    head := list

    for list1 != nil && list2 != nil {

        value1 := list1.Val
        value2 := list2.Val

        if value1 > value2 {
            list.Next = &ListNode{value2, nil}
            list = list.Next
            list2 = list2.Next
        } else {
            list.Next = &ListNode{value1, nil}
            list = list.Next
            list1 = list1.Next
        }
    }

     if list1 != nil {
        list.Next = list1
    } else {
        list.Next = list2
    }
    
    return head.Next
}
