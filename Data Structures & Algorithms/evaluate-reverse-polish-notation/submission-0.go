type Stack struct {
    data []int
}

func (s *Stack) Pop() int {
    number := s.data[len(s.data)-1]
    s.data = s.data[:len(s.data)-1]
    return number
}

func (s *Stack)  Push(n int) {
    s.data = append(s.data, n)
}

func evalRPN(tokens []string) int {
    stack := Stack{[]int{}}

    for _, t := range tokens {
        fmt.Println(stack, t)
        if t == "+" || t == "-" || t == "*" || t == "/" {
            DoOperation(&stack, t)
        } else {
            n, _ := strconv.Atoi(t)
            stack.Push(n)
        }
    }
    return stack.Pop()
}

func DoOperation(s *Stack, o string) {
    n1 := s.Pop()
    n2 := s.Pop()
    switch o {
        case "+": s.Push(n2+n1)
        case "-": s.Push(n2-n1)
        case "*": s.Push(n2*n1)
        case "/": s.Push(n2/n1)
    }
}
