class MinStack:
    stack = []
    min_stack = []

    # @param x, an integer
    def push(self, x):
        self.stack.append(x)

        if len(self.min_stack) > 0:
            if x <= self.min_stack[-1]:
                self.min_stack.append(x)
        else:
            self.min_stack.append(x)

    # @return nothing
    def pop(self):
        if len(self.stack) == 0:
            return

        x = self.stack.pop()
        
        if len(self.min_stack) > 0 and x == self.min_stack[-1]:
            self.min_stack.pop()

    # @return an integer
    def top(self):
        if len(self.stack) == 0:
            return -1

        return self.stack[-1]

    # @return an integer
    def getMin(self):
        if len(self.min_stack) == 0:
            return -1

        return self.min_stack[-1]

if __name__ == '__main__':
    ms = MinStack()
    assert(ms.getMin() == -1)
    assert(ms.top() == -1)
    assert(ms.top() == -1)
    assert(ms.getMin() == -1)

    ms.push(5)
    ms.push(8)
    ms.push(2)
    ms.push(1)
    ms.pop()
    ms.pop()

    assert(ms.getMin() == 5)
    assert(ms.top() == 8)    

    
