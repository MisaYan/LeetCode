class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.mini = list()

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.mini or x <= self.mini[-1]:
            self.mini.append(x)

    def pop(self) -> None:
        if self.stack.pop() == self.mini[-1]:
            self.mini.pop()


    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.mini[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
