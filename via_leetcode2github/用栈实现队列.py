class MyQueue:

    def __init__(self):
        #先进先出：FILO —— 队列  #后进先出：LIFO —— 栈
        """
        Initialize your data structure here.
        """
        self.input = []
        self.output = []



    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while self.output:
            self.input.append(self.output.pop())
        self.input.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while self.input:
            self.output.append(self.input.pop())
        return self.output.pop(-1)


    def peek(self) -> int:
        """
        Get the front element.
        """
        while self.input:
            self.output.append(self.input.pop())
        return self.output[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.input and not self.output



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
