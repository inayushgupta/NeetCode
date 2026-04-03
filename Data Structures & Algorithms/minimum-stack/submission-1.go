type MinStack struct {
    data [][]int
}

func Constructor() MinStack {
    return MinStack{[][]int{},}
}

func (this *MinStack) Push(val int) {
    if len(this.data) == 0 {
        // this will push the first element to the stack.
        // first element is for now the minimum element of the stack
        this.data = append(this.data, []int{val, val})
    } else {
        prevMin := this.data[len(this.data)-1][1]
        if prevMin > val {
            this.data = append(this.data, []int{val, val})
        } else {
            this.data = append(this.data, []int{val, prevMin})
        }
    }
}

func (this *MinStack) Pop() {
    this.data = this.data[:len(this.data) - 1]
}

func (this *MinStack) Top() int {
    return this.data[len(this.data) - 1][0]
}

func (this *MinStack) GetMin() int {
    return this.data[len(this.data) - 1][1]
}
