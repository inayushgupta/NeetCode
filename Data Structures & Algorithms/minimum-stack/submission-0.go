type MinStack struct {
    data [][]int
}

func Constructor() MinStack {
    return MinStack{[][]int{}}
}

func (this *MinStack) Push(val int) {
    if len(this.data) == 0 {
        this.data = [][]int{ {val, val}, }
    } else {
        // check if the new value is the new minimum or not
        prevMin := this.data[len(this.data) - 1][1]
        if prevMin < val {
            this.data = append(this.data, []int{val, prevMin})
        } else {
            this.data = append(this.data, []int{val, val})
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
