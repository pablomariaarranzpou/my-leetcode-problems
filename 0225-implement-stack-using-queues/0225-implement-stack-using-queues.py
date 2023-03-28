class MyStack:

    def __init__(self):
        self.obj = []

    def push(self, x: int) -> None:
        self.obj.append(x)
        

    def pop(self) -> int:
        return self.obj.pop()
        

    def top(self) -> int:
        return self.obj[-1]

        
    def empty(self) -> bool:
        return self.obj == []
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()