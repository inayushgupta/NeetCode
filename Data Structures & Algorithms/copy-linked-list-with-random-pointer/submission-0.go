/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Next *Node
 *     Random *Node
 * }
 */

func copyRandomList(head *Node) *Node {
    dummy := &Node{0, nil, nil}
    newList := dummy

    pointers := make(map[*Node]*Node)
    pointers[nil] = nil 

    for head != nil {
        val := head.Val
        newNode := &Node{val, nil, head.Random}
        pointers[head] = newNode
        dummy.Next = newNode
        dummy = dummy.Next
        head = head. Next
    }

    dummy = newList.Next

    for dummy != nil {
        newPointer := pointers[dummy.Random]
        dummy.Random = newPointer
        dummy = dummy.Next
    }

    return newList.Next
}
