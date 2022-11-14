class RecentCounter:

    def __init__(self):
        self.calls = []
        

    def ping(self, t: int) -> int:
        min = t - 3000
        self.calls.append(t);
        
        ans = []
        for c in self.calls:
            if c >= min:
                ans.append(c)
        
        self.calls = ans
        return len(self.calls)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)