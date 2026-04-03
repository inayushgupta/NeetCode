func dailyTemperatures(t []int) []int {
    stack := Stack{[][]int{}}
    res := make([]int, len(t), len(t))

    for i, n := range t {
        if len(stack.data) == 0 {
            stack.Push(n, i)
        }


        for len(stack.data) != 0  {
            topNum, topIndex := stack.Top()
            if n <= topNum {
                break
            }
            res[topIndex] = i - topIndex
            stack.Pop()
        }

        stack.Push(n, i)
    }
    fmt.Println(stack)
    return res
}

type Stack struct {
    data [][]int
}

func (s *Stack) Pop() {
    s.data = s.data[:len(s.data)-1]
}

func (s *Stack) Top() (int, int) {
    ans := s.data[len(s.data)-1]
    return ans[0], ans[1]
}

func (s *Stack)  Push(n, i int) {
    s.data = append(s.data, []int{n, i})
}