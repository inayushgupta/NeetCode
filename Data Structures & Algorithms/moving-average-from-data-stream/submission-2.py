class MovingAverage:

    def __init__(self, size: int):
        self.running_sum = 0
        self.data = collections.deque()
        self.size = size
        self.curr = 0

    def next(self, val: int) -> float:
        if len(self.data) < self.size:
            self.data.append(val)
            self.running_sum += val
        else:
            self.running_sum += val - self.data.popleft()
            self.data.append(val)
        return self.running_sum/len(self.data)
        
        

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
