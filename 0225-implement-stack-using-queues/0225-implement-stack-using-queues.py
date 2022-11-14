class MyStack:

    def __init__(self):
        self.q1 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        q2 = deque()
       
        while len(self.q1) > 1:
            q2.append(self.q1.popleft())
        
        ans = self.q1[0]
        self.q1.popleft()
        self.q1 = q2;
        
        return ans
    
    def top(self) -> int:
        return self.q1[-1]
        

    def empty(self) -> bool:
        return len(self.q1) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()