import "errors"

type Stack struct {
    data []string
}

func (s *Stack) Push(str string) {
    s.data = append(s.data, str) 
}

func (s *Stack) Pop() (string, error) {
    if len(s.data) == 0 {
        return "", errors.New("Stack is empty")
    } else {
        temp := s.data[len(s.data) - 1]
        s.data = s.data[:len(s.data)-1]
        return temp, nil
        
    }
    return "", nil
}

// push to the stack if it is a opening bracket
// if the element is a closing bracket then pop
// if the element is equal then continue otherwise 
// throw quit the function and return false

func isOpening(b string) bool {
    return b == "{" || b == "[" || b == "("
}

func returnOpening(b string) string {
    switch b {
        case "}": 
            return "{"
        case "]":
            return "["
        case ")":
            return "("
    }
    return ""
} 

func CheckCounter(openB, closeB string) bool {
    if returnOpening(closeB) == openB {
        return true
    }

    return false
}

func (s *Stack) IsEmpty() bool {
    if len(s.data) == 0 {
        return true
    } else {
        return false
    }
}

// [  ]
func isValid(s string) bool {
    stack := Stack{data: []string{}}
    ans := true
    for i, b := range s {
        fmt.Println(i, stack.data, string(b), s)
        if !isOpening(string(b)) {
            ele, err := stack.Pop()
            fmt.Println("pop", ele, err)
            if err != nil {
                fmt.Println("error!")
                ans = false
                break
            }
            complete := CheckCounter(ele, string(b))
            if complete {
                continue
            } else {
                ans = false
                break
            }
        } else {
            stack.Push(string(b))
        }
    }

    return ans && stack.IsEmpty()
}
