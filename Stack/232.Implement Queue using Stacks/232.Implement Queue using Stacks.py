class MyQueue:

    def __init__(self):
        self.stack = []
        self.re = []
    def push(self, x: int) -> None:
        self.stack.append(x)
    def pop(self) -> int:
        while (self.stack!=[]):
            self.re.append(self.stack.pop())
        delt = self.re.pop()
        while (self.re!=[]):
            self.stack.append(self.re.pop())
        return delt
    def peek(self) -> int:
        return self.stack[0]
    def empty(self) -> bool:
        return self.stack == []

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()