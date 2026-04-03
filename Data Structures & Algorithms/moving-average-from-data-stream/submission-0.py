class MovingAverage:

    def __init__(self, size: int):
        self.data = [0]*size
        self.size = size
        self.curr = 0
        

    def next(self, val: int) -> float:
        self.edit_value(val)
        self.curr = self.curr+1 if self.curr < self.size else self.size
        return sum(self.data)/self.curr


    def edit_value(self, val):
        self.data.append(val)
        self.data = self.data[1:]
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
