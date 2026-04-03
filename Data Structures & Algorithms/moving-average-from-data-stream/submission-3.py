class MovingAverage:

    def __init__(self, size: int):
        self.data = collections.deque()
        self.running_sum = 0
        self.size = size

    def next(self, val: int) -> float:
        if len(self.data) == self.size:
            self.running_sum -= self.data.popleft()
        self.running_sum += val
        self.data.append(val)
        return self.running_sum/len(self.data)
        
        

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
