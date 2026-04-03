class MovingAverage:

    def __init__(self, size: int):
        self.running_sum = 0
        self.data = collections.deque()
        self.size = size
        self.curr = 0

    def next(self, val: int) -> float:
        if self.curr < self.size:
            self.data.append(val)
            self.running_sum += val
            self.curr+=1
        else:
            popped = self.data.popleft()
            self.running_sum = self.running_sum - popped + val
            self.data.append(val)
            self.curr = self.size
        return self.running_sum/self.curr
        
        

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
