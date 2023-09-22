class MinStack:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, value):
        if len(self.s1) == 0:
            self.s1.append(value)
        
        self.s1.append(min(value, self.s1[-1]))
        self.s2.append(value)
        return

    def pop(self):
        self.s1.pop(-1)
        return self.s2.pop(-1)

    def getMin(self):
        return self.s1[-1]
